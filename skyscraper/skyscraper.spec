%global gittag 3.9.0

Name:    skyscraper
Version: 3.9.0
Release: 1%{?dist}
Summary: Powerful and versatile game scraper

# The source files say 2 or later, but the LICENSE file it comes with is v3, so go with v3
License: GPL-3.0-or-later
URL:     https://github.com/Gemba/skyscraper
Source0: https://github.com/Gemba/skyscraper/archive/%{gittag}/%{name}-%{version}.tar.gz

Patch0:  0001-Remove-hardcoded-paths.patch
Patch1:  0002-Remove-the-supplementary-install.patch

Patch3:  0001-Add-additional-screenscraper-platforms.patch
Patch4:  0002-Split-satellaview-and-sufami-turbo-out-of-snes.patch

BuildRequires: gcc-c++
BuildRequires: qt5-qtbase-devel

%description
A powerful and versatile yet easy to use game scraper written in C++ for use
with multiple frontends running on a Linux system (macOS and Windows too, but
not officially supported). It scrapes and caches various game resources from
various scraping sources, including media such as screenshot, cover and video.
It then gives you the option to generate a game list and artwork for the chosen
frontend by combining all of the cached resources.

%prep
%autosetup -p1

%build
%qmake_qt5 BINDIR=%{_bindir} CONFDIR=%{_sysconfdir}/skyscraper
make %{?_smp_mflags}

%install
%make_install INSTALL_ROOT=%{buildroot}

%files
%doc README.md
%license LICENSE
%{_bindir}/Skyscraper
%config %{_sysconfdir}/skyscraper

%changelog
* Thu Oct 26 2023 David Shea <reallylongword@gmail.com> - 3.9.0-1
- Update to 3.9.0

* Mon Oct 23 2023 David Shea <reallylongword@gmail.com> - 3.7.7-7
- Add sufami turbo and satellaview as separate platforms

* Wed Mar  8 2023 David Shea <reallylongword@gmail.com> - 3.7.7-6
- Add GX4000

* Sun Mar  5 2023 David Shea <reallylongword@gmail.com> - 3.7.7-5
- Add Super Cassette Vision support

* Sun Mar  5 2023 David Shea <reallylongword@gmail.com> - 3.7.7-4
- Add PV-1000 support

* Sat Mar  4 2023 David Shea <reallylongword@gmail.com> - 3.7.7-3
- Add Adventure Vision support

* Tue Feb 28 2023 David Shea <reallylongword@gmail.com> - 3.7.7-2
- Add CreatiVision support

* Mon Feb 27 2023 David Shea <reallylongword@gmail.com> - 3.7.7-1
- Initial package
