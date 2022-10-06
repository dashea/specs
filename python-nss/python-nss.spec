%global hgrev 9de14a6f77e2586269e91f770ca7f7b95282945d
%global hgshortrev 9de14a6f77e2

Name:    python-nss
Version: 1.0.1^20210803hg%{hgshortrev}
Release: 1%{?dist}
Summary: Python bindings for Network Security Services (NSS)

License: MPLv2.0 or GPLv2+ or LGPLv2+
URL:     https://firefox-source-docs.mozilla.org/security/nss/legacy/python_binding_for_nss/index.html

# There is a pypi package, but it does not include docs. hg.mozilla.org is the upstream VCS.
# This is a snapshot of the current hg tip, three commits ahead of PYNSS_RELEASE_1_0_1
Source0: https://hg.mozilla.org/projects/python-nss/archive/%{hgrev}.zip

Patch1: 0001-Remove-the-docs-build-from-setup.py.patch
Patch2: 0002-Remove-the-version-number-from-setup.py.patch
Patch3: 0003-Use-pkgconfig-to-find-nss-and-nspr.patch
Patch4: 0004-Switch-to-setuptools.patch
Patch5: 0005-Convert-the-tests-to-pytest.patch

BuildRequires: gcc
BuildRequires: python3-devel
BuildRequires: nss-devel

# Needed for tests
BuildRequires: nss-tools

# Needed for docs
BuildRequires: /usr/bin/sphinx-build

%global _description %{expand:
This package provides Python bindings for Network Security Services
(NSS) and the Netscape Portable Runtime (NSPR).

NSS is a set of libraries supporting security-enabled client and
server applications. Applications built with NSS can support SSL v2
and v3, TLS, PKCS #5, PKCS #7, PKCS #11, PKCS #12, S/MIME, X.509 v3
certificates, and other security standards. Specific NSS
implementations have been FIPS-140 certified.}

%description %_description

%package -n python3-nss
Summary: %{summary}

%description -n python3-nss %_description

%prep
%autosetup -n python-nss-%{hgrev} -p1

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files nss

# The tox macro uses buildroot as the env, so this needs to happen after install
%tox -e docs

mkdir -p %{buildroot}%{_docdir}%{name}/html
mv .tox/docs_out html

%check
%tox

%files -n python3-nss -f %{pyproject_files}
%license LICENSE.gpl LICENSE.lgpl LICENSE.mpl
%doc README html

%changelog
* Fri Sep 30 2022 David Shea <reallylongword@gmail.com> - 1.0.1^20210803hg9de14a6f77e2
- Restore the python-nss package
- Start from the upstream hg tip
- Modernize the build process to use a PEP517/518 style build
- Modernize the spec file
