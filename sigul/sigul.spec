Summary: A signing server and related software client
Name: sigul

# Using the upstream master commit as the snapshot ID
Version: 1.1^20220718gita6dc475
Release: 1.dshea1%{?dist}
License: GPLv2

URL: https://pagure.io/sigul/

# The github repo is a fork of https://pagure.io/sigul.git from commit a6dc475
%global commit d5e58a069ab482b6b4ca23d495cb400e1f32f20f
%global shortcommit d5e58a0
Source0: https://github.com/dashea/sigul/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

Source1: sigul_bridge.service
Source2: sigul_server.service
Source3: sigul.logrotate
Source4: sigul.conf

# Since this package is building python via autotools, it uses the "legacy" packaging standard,
# and also the automatic dependency generation is not helpful. Make everything manual.
%{?python_disable_dependency_generator}

BuildRequires: systemd-rpm-macros
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: gcc
BuildRequires: python3-devel

# Programs called from python and sigul_setup_client
BuildRequires: /usr/bin/certutil
BuildRequires: /usr/bin/pk12util
BuildRequires: /usr/bin/gpg
BuildRequires: /usr/bin/tpm_sealdata
BuildRequires: /usr/bin/tpm_unsealdata
BuildRequires: /usr/bin/openssl
BuildRequires: /usr/bin/keyctl
BuildRequires: /usr/bin/rpm
BuildRequires: /usr/bin/rpmsign
BuildRequires: /usr/bin/gpg

# Python requirements
BuildRequires: %{py3_dist cryptography}
BuildRequires: %{py3_dist gpg}
BuildRequires: %{py3_dist koji}
BuildRequires: %{py3_dist python-nss}
BuildRequires: %{py3_dist requests}
BuildRequires: %{py3_dist rpm}
BuildRequires: %{py3_dist six}
BuildRequires: %{py3_dist six}
BuildRequires: %{py3_dist sqlalchemy}

# Requirement for ostree helper
BuildRequires: pkgconfig(ostree-1)

# Additional test requirements:
# analysis.at
BuildRequires: /usr/bin/bandit
BuildRequires: /usr/bin/pycodestyle-3
# file-signing.at
BuildRequires: /usr/bin/evmctl
# ostree.at
BuildRequires: /usr/bin/ostree
# sign-rpms.at
BuildRequires: /usr/bin/rpmbuild

# Skopeo uses go and is only built on arches where go is supported
BuildRequires: go-srpm-macros
%ifarch %{go_arches}
BuildRequires: skopeo
%endif

# Required by extract_img_signatures in testtools
BuildRequires: rust-srpm-macros
%ifarch %{rust_arches}
BuildRequires: (crate(rpm-rs) >= 0.8.1 with crate(rpm-rs) < 0.9.0~)
BuildRequires: (crate(hex) >= 0.4.2 with crate(hex) < 0.5.0~)
%endif

%description
A signing server, which lets authorized users sign data without having any
access to the necessary private key, a client for the server, and a "bridge"
that connects the two.

%package ostree-helper
Summary: Sigul OSTree helper

%description ostree-helper
This package contains a OSTree helper program used by sigul-server.

%package server
Summary: Sigul server component
Requires: %{name}-common = %{version}-%{release}
Requires: %{name}-ostree-helper = %{version}-%{release}
BuildArch: noarch

Requires: /usr/bin/rpm
Requires: /usr/bin/rpmsign
Requires: /usr/bin/gpg

Requires: %{py3_dist six}
Requires: %{py3_dist cryptography}
Requires: %{py3_dist python-nss}
Requires: %{py3_dist rpm}
Requires: %{py3_dist sqlalchemy}
Requires: %{py3_dist gpg}
Requires: python(abi) = %{python3_version}

%description server
The server part of sigul that keeps the keys and performs the actual signing.


%package bridge
Summary: Sigul bridge
Requires: %{name}-common = %{version}-%{release}
BuildArch: noarch

Requires: %{py3_dist six}
Requires: %{py3_dist fedora}
Requires: %{py3_dist python-nss}
Requires: %{py3_dist koji}
Requires: %{py3_dist rpm}
Requires: python(abi) = %{python3_version}

%description bridge
The bridge part of sigul that facilitates connection between the client and server.

%package common
Summary: Sigul common files
BuildArch: noarch

Requires: /usr/bin/tpm_sealdata
Requires: /usr/bin/tpm_unsealdata
Requires: /usr/bin/openssl
Requires: /usr/bin/keyctl

Requires: %{py3_dist six}
Requires: %{py3_dist python-nss}
Requires: %{py3_dist koji}
Requires: python(abi) = %{python3_version}

%description common
Common files for sigul.

%package client
Summary: Sigul client
Requires: %{name}-common = %{version}-%{release}
BuildArch: noarch

%description client
The client CLI for Sigul.

%prep
%setup -q -n sigul-%{commit}

%build
autoreconf -i
PYTHON=/usr/bin/python3 %configure --with-ostree
%make_build

%check
make check

%install
%make_install
mkdir -p %{buildroot}%{_unitdir} %{buildroot}%{_sysconfdir}/logrotate.d
install -m 0644 -p %{SOURCE1} %{buildroot}%{_unitdir}/sigul_bridge.service
install -m 0644 -p %{SOURCE2} %{buildroot}%{_unitdir}/sigul_server.service
install -m 0644 -p %{SOURCE3} %{buildroot}%{_sysconfdir}/logrotate.d/sigul
install -p -D -m 0644 %{SOURCE4} %{buildroot}%{_sysusersdir}/sigul.conf

%pre
%sysusers_create_compat %{SOURCE4}

%post bridge
%systemd_post sigul_bridge.service

%post server
%systemd_post sigul_server.service

%preun bridge
%systemd_preun sigul_bridge.service

%preun server
%systemd_preun sigul_server.service

%postun bridge
%systemd_postun_with_restart sigul_bridge.service

%postun server
%systemd_postun_with_restart sigul_server.service


%files common
%doc AUTHORS COPYING NEWS README
%config(noreplace) %{_sysconfdir}/logrotate.d/sigul
%dir %{_datadir}/sigul
%dir %{_sysconfdir}/sigul
%{_datadir}/sigul/bind_methods.py*
%{_datadir}/sigul/double_tls.py*
%{_datadir}/sigul/errors.py*
%{_datadir}/sigul/settings.py*
%{_datadir}/sigul/utils.py*
%{_datadir}/sigul/__pycache__/bind_methods.*
%{_datadir}/sigul/__pycache__/double_tls.*
%{_datadir}/sigul/__pycache__/errors.*
%{_datadir}/sigul/__pycache__/settings.*
%{_datadir}/sigul/__pycache__/utils.*
%{_sysusersdir}/sigul.conf

%files client
%config(noreplace) %{_sysconfdir}/sigul/client.conf
%{_bindir}/sigul
%{_bindir}/sigul_setup_client
%{_mandir}/man1/sigul.1*
%{_mandir}/man1/sigul_setup_client.1*
%{_datadir}/sigul/client.py*
%{_datadir}/sigul/__pycache__/client.*

%files bridge
%config(noreplace) %attr(640,root,sigul) %{_sysconfdir}/sigul/bridge.conf
%{_unitdir}/sigul_bridge.service
%{_sbindir}/sigul_bridge
%{_datadir}/sigul/bridge*
%{_datadir}/sigul/bridge.py*
%{_datadir}/sigul/__pycache__/bridge.*
%{_mandir}/man8/sigul_bridge.8*

%files server
%config(noreplace) %attr(640,root,sigul) %{_sysconfdir}/sigul/server.conf
%{_unitdir}/sigul_server.service
%{_sbindir}/sigul_server
%{_sbindir}/sigul_server_add_admin
%{_sbindir}/sigul_server_create_db
%dir %attr(700,sigul,sigul) %{_localstatedir}/lib/sigul
%dir %attr(700,sigul,sigul) %{_localstatedir}/lib/sigul/gnupg
%{_datadir}/sigul/server*
%{_datadir}/sigul/__pycache__/server*
%{_mandir}/man8/sigul_server.8*
%{_mandir}/man8/sigul_server_add_admin.8*
%{_mandir}/man8/sigul_server_create_db.8*

%files ostree-helper
%{_bindir}/sigul-ostree-helper

%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.1-3
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 13 2021 Patrick Uiterwijk <patrick@puiterwijk.org> - 1.1-1
- Rebase to v1.1

* Sat Dec 05 2020 Kevin Fenzi <kevin@scrye.com> - 1.0a1-5
- Drop no longer needed _python_bytecompile_extra

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0a1-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0a1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 09 2020 Patrick Uiterwijk <patrick@puiterwijk.org> - 1.0a1-2
- Add server_gpg.py

* Tue Jun 09 2020 Patrick Uiterwijk <patrick@puiterwijk.org> - 1.0a1-1
- Rebase to v1.0a1
- Added support for Python3 (and probably dropped Py3)
- Added support for GPGv2

* Mon Apr 06 2020 Mohan Boddu <mboddu@bhujji.com> - 0.207-10
- Fixing build failures

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.207-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.207-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.207-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.207-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 28 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.207-5
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.207-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.207-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.207-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu May 04 2017 Patrick Uiterwijk <puiterwijk@redhat.com> - 0.207-1
- Rebase to 0.207

* Wed May 03 2017 Patrick Uiterwijk <puiterwijk@redhat.com> - 0.206-2
- Koji was broken. Rebuild please

* Tue May 02 2017 Patrick Uiterwijk <puiterwijk@redhat.com> - 0.206-1
- Rebase to 0.206

* Wed Mar 01 2017 Patrick Uiterwijk <puiterwijk@redhat.com> - 0.205-1
- Rebase to upstream 0.205

* Tue Feb 21 2017 Patrick Uiterwijk <puiterwijk@redhat.com> - 0.204-3
- Add PIN reading fix

* Tue Feb 21 2017 Patrick Uiterwijk <puiterwijk@redhat.com> - 0.204-2
- rebuilt

* Mon Feb 20 2017 Patrick Uiterwijk <puiterwijk@redhat.com> - 0.204-1
- Rebase to upstream 0.204

* Mon Feb 13 2017 Patrick Uiterwijk <puiterwijk@redhat.com> - 0.203-1
- Rebase to 0.203

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.202-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Dec 11 2016 Patrick Uiterwijk <puiterwijk@redhat.com> - 0.202-4
- Add patch for krb5 support

* Sat Oct 29 2016 Patrick Uiterwijk <puiterwijk@redhat.com> - 0.202-3
- Disable test suite for ppc64, since skopeo failed to build
- Enable test suite on Fedora instead of RHEL

* Wed Oct 19 2016 Patrick Uiterwijk <puiterwijk@redhat.com> - 0.202-2
- Do not run tests on el7

* Tue Oct 11 2016 Patrick Uiterwijk <puiterwijk@redhat.com> - 0.202-1
- Update to 0.202

* Tue Sep 20 2016 Patrick Uiterwijk <puiterwijk@redhat.com> - 0.201-2
- Rebuild with test suite on

* Fri Sep 16 2016 Patrick Uiterwijk <puiterwijk@redhat.com> - 0.201-1
- New upstream release

* Wed Sep 07 2016 Patrick Uiterwijk <puiterwijk@redhat.com> - 0.200-1
- New upstream release

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.102-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 25 2016 Miloslav Trmač <mitr@redhat.com> - 0.102-2
- Migrate to systemd unit files, based on a patch by Kevin Fenzi
  <kevin@scrye.com>.
  Resolves: #1301297

* Thu Nov 26 2015 Miloslav Trmač <mitr@redhat.com> - 0.102-1
- Update to sigul-0.102.
  Resolves: #1283364
  Related: #1272535

* Wed Nov 18 2015 Miloslav Trmač <mitr@redhat.com> - 0.101-1
- Update to sigul-0.101.
  Related: #1272535

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.100-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Apr 27 2015 Miloslav Trmač <mitr@redhat.com> - 0.100-5
- Add Requires: rpm-sign
  Resolves: #1215678

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.100-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.100-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.100-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jul 17 2012 Miloslav Trmač <mitr@redhat.com> - 0.100-1
- Update to sigul-0.100.

* Wed Feb  8 2012 Toshio Kuratomi <toshio@fedoraproject.org> - 0.99-3
- Remove the python-sqlite2 dep in Fedora as that package is being retired and
  sigul can use the sqlite3  module from the python stdlib

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jun  6 2011 Miloslav Trmač <mitr@redhat.com> - 0.99-1
- Update to sigul-0.99.

* Thu Jun  2 2011 Miloslav Trmač <mitr@redhat.com> - 0.98-2
- Add Requires: gnupg
  Resolves: #664536

* Tue May 31 2011 Miloslav Trmač <mitr@redhat.com> - 0.98-1
- Update to sigul-0.98.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.97-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Aug 11 2010 David Malcolm <dmalcolm@redhat.com>
- recompiling .py files against Python 2.7 (rhbz#623359)

- Drop no longer necessary references to BuildRoot:

* Fri Jul 31 2009 Miloslav Trmač <mitr@redhat.com> - 0.97-1
- Update to sigul-0.97.
- Ship NEWS.

* Tue Jul 28 2009 Jesse Keating <jkeating@redhat.com> - 0.96-6
- Fix the patch in -4

* Tue Jul 28 2009 Jesse Keating <jkeating@redhat.com> - 0.96-5
- Add a dist tag

* Tue Jul 28 2009 Jesse Keating <jkeating@redhat.com> - 0.96-4
- Add another patch to temporarily work around a stale koji issue.
- Bump python-nss reqs up now that we have a newer one in EPEL

* Mon Jul 27 2009 Jesse Keating <jkeating@redhat.com> - 0.96-3
- Setup the Requires right for EL5

* Mon Jul 27 2009 Jesse Keating <jkeating@redhat.com> - 0.96-2
- Fix various bugs while testing (release by Mitr)
- Patch from jkeating for srpm signing.

* Sat Jul 18 2009 Miloslav Trmač <mitr@redhat.com> - 0.95-0.mitr.1
- Update to 0.95.
- Add missing Requires: m2crypto.

* Wed Jul  1 2009 Miloslav Trmač <mitr@redhat.com> - 0.94-0.mitr.1
- Update to 0.94.

* Fri Apr 10 2009 Miloslav Trmač <mitr@redhat.com> - 0.93-0.mitr.1
- Update to 0.93.

* Wed Jan 28 2009 Miloslav Trmač <mitr@redhat.com> - 0.92-0.mitr.1
- Update to 0.92.

* Mon Jan 12 2009 Miloslav Trmač <mitr@redhat.com> - 0.91-0.mitr.1
- Update to 0.91.

* Sun Jan 11 2009 Miloslav Trmač <mitr@redhat.com> - 0.90-0.mitr.2
- Requires: koji, python-sqlite2

* Sun Jan 11 2009 Miloslav Trmač <mitr@redhat.com> - 0.90-0.mitr.1
- s/rpmsigner/sigul/g

* Sun Nov 30 2008 Miloslav Trmač <mitr@redhat.com> - 0.90-0.mitr.1
- Initial package.
