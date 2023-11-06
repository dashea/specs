%global commit b10c59fc40a6928a0b2d8766fa8b0323cf3f9ba7
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:    woz2dsk
Version: 0
Release: 1^20230717git%{shortcommit}%{?dist}
Summary: A utility for converting .woz files to .dsk, .po and .nib files

License: GPL-3.0-or-later
URL:     https://github.com/leesaudan2/woz2dsk
Source0: https://github.com/leesaudan2/woz2dsk/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildArch: noarch
BuildRequires: perl-generators

%description
woz2dsk is a utility for converting .woz files to .dsk, .po and .nib
files.  These formats are widely used by Apple II emulators.


%prep
%autosetup -n woz2dsk-%{commit}


%build
# nothing to build

%install
mkdir -p %{buildroot}/%{_bindir}
install -m 0755 woz2dsk %{buildroot}/%{_bindir}/woz2dsk

%files
%doc README.md
%license LICENSE.txt
%{_bindir}/woz2dsk

%changelog
* Mon Nov  6 2023 David Shea <reallylongword@gmail.com> - 0-1^20230717gitb10c59f
- Initial package
