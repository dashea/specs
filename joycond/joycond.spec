%global gitcommit 5b590ecc9bca181d8bc21377e752126bc9180319
%global shortcommit 5b590ec

Name:    joycond
Version: 0.1.0^20220720git%{shortcommit}
Release: 1%{?dist}
Summary: A daemon to implement joycon pairing

License: GPLv3
URL:     https://github.com/DanielOgorchock/joycond
Source0: https://github.com/DanielOgorchock/joycond/archive/%{gitcommit}/%{name}-%{shortcommit}.tar.gz
Patch0:  0001-Skip-installing-systemd-and-udev-files.patch

BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: pkgconfig(libevdev)
BuildRequires: pkgconfig(libudev)

%description
joycond is a linux daemon which uses the evdev devices provided by hid-nintendo (formerly known as hid-joycon) to implement joycon pairing.

%prep
%autosetup -n joycond-%{gitcommit}

%build
%cmake
%cmake_build

%install
%cmake_install

mkdir -p %{buildroot}%{_unitdir}
install -m 0644 -p systemd/joycond.service %{buildroot}%{_unitdir}/joycond.service

mkdir -p %{buildroot}%{_modulesloaddir}
install -m 0644 -p systemd/joycond.conf %{buildroot}%{_modulesloaddir}/joycond.conf

mkdir -p %{buildroot}%{_udevrulesdir}
install -m 0644 -p udev/89-joycond.rules %{buildroot}%{_udevrulesdir}/89-joycond.rules
install -m 0644 -p udev/72-joycond.rules %{buildroot}%{_udevrulesdir}/72-joycond.rules

%post
%systemd_post joycond.service

%preun
%systemd_preun joycond.service

%postun
%systemd_postun joycond.postun

%files
%doc README.md
%license LICENSE
%{_modulesloaddir}/joycond.conf
%{_unitdir}/joycond.service
%{_udevrulesdir}/72-joycond.rules
%{_udevrulesdir}/89-joycond.rules
%{_bindir}/joycond

%changelog
* Sun Aug 14 2022 David Shea <reallylongword@gmail.com> - 0.1.0^20220720git5b590ec
- Initial version

