%global gittag 3.7.7

Name:    skyscraper
Version: 3.7.7
Release: 1%{?dist}
Summary: Powerful and versatile game scraper

# The source files say 2 or later, but the LICENSE file it comes with is v3, so go with v3
License: GPL-3.0-or-later
URL:     https://github.com/muldjord/skyscraper
Source0: https://github.com/muldjord/skyscraper/archive/%{gittag}/%{name}-%{version}.tar.gz

Patch0:  0001-Remove-hardcoded-paths.patch

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
%qmake_qt5 BINDIR=%{_bindir} CONFDIR=%{_sysconfdir}
make %{?_smp_mflags}

%install
%make_install INSTALL_ROOT=%{buildroot}

%files
%doc README.md
%license LICENSE
%{_bindir}/Skyscraper
%config %{_sysconfdir}/skyscraper

%changelog
* Mon Feb 27 2023 David Shea <reallylongword@gmail.com> - 3.7.7-1
- Initial package
