Name:    xcape
Version: 1.2
Release: 1%{?dist}
Summary: Remap modifier keys to act as other keypresses

License: GPL-3.0-or-later
URL:     https://github.com/alols/xcape
Source0: https://github.com/alols/xcape/archive/refs/tags/v1.2.tar.gz

BuildRequires: gcc
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xtst)

%description
xcape allows you to use a modifier key as another key when pressed and released
on its own. Note that it is slightly slower than pressing the original key,
because the pressed event does not occur until the key is released. The default
behaviour is to generate the Escape key when Left Control is pressed and
released on its own. (If you don't understand why anybody would want this, I'm
guessing that Vim is not your favourite text editor ;)

%prep
%autosetup


%build
make %{?_smp_mflags}


%install
# The makefile is hand-written, and deviates from autoconf-ish behavior just enough to break use of directory macros
# It's only two files, do it by hand
install -m 0755 -D xcape %{buildroot}%{_bindir}/xcape
install -m 0644 -D xcape.1 %{buildroot}%{_mandir}/man1/xcape.1


%files
%doc README.md
%license LICENSE
%{_bindir}/xcape
%{_mandir}/man1/xcape.1*


%changelog
* Mon Apr  8 2024 David Shea <reallylongword@gmail.com> - 1.2-1
- Initial package
