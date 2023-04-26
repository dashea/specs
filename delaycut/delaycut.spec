%global gittag v1.4.3.10

Name:    delaycut
Version: 1.4.3.10
Release: 1%{?dist}
Summary: Cuts and corrects delay in ac3 and dts files

License: GPL-3.0-only
URL:     https://github.com/darealshinji/delaycut
Source0: https://github.com/darealshinji/delaycut/archive/%{gittag}/%{name}-%{version}.tar.gz

BuildRequires: gcc-c++
BuildRequires: qt5-qtbase-devel

%description
Cuts and corrects delay in ac3 and dts files

%prep
%autosetup

%build
%qmake_qt5
make %{?_smp_mflags}

%install
# disable the strip command to allow rpmbuild to handle debug symbols
%make_install INSTALL_ROOT=%{buildroot} STRIP=true

%files
%doc README ChangeLog docs/AC3-Specifications-ts_102366v010401p.pdf
%license COPYING
%{_bindir}/delaycut

%changelog
* Wed Apr 26 2023 David Shea <reallylongword@gmail.com> - 1.4.3.10-1
- Initial version
