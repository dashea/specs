Name:    xa
Version: 2.3.14
Release: 1%{?dist}
Summary: A high-speed, two-pass portable 6502 cross-assembler

License: GPL-2.0-or-later
URL:     https://www.floodgap.com/retrotech/xa/

Source0: https://www.floodgap.com/retrotech/xa/dists/xa-2.3.14.tar.gz

Patch0: fix-man-permissions.patch
Patch1: use-ldflags-for-misc.patch

BuildRequires: gcc
BuildRequires: /usr/bin/iconv

%description
xa (xa65) is a high-speed, two-pass portable cross-assembler. It understands
mnemonics and generates code for NMOS 6502s (such as 6502A, 6504, 6507, 6510,
7501, 8500, 8501, 8502 ...), CMOS 6502s (65C02 and Rockwell R65C02) and the
65816.

%prep
%autosetup -p1

# Fix all the non-utf8 text files
iconv -f latin1 -t utf8 -o ChangeLog.utf8 ChangeLog
mv ChangeLog.utf8 ChangeLog

iconv -f latin1 -t utf8 -o fileformat.utf8 doc/fileformat.txt
mv fileformat.utf8 doc/fileformat.txt

iconv -f latin1 -t utf8 -o xa-de.utf8 doc/xa-de.log
mv xa-de.utf8 doc/xa-de.log

iconv -f latin1 -t utf8 -o xa-de.utf8 doc/xa-de.txt
mv xa-de.utf8 doc/xa-de.txt

iconv -f latin1 -t utf8 -o xa.utf8 doc/xa.log
mv xa.utf8 doc/xa.log

iconv -f latin1 -t utf8 -o xaannounce.utf8 doc/xaannounce
mv xaannounce.utf8 doc/xaannounce


%build
# not automake, set the variables in the environment then tell make to prefer environment over Makefile
%set_build_flags
make %{?_smp_mflags} -e


%install
# not automake, set paths by hand
%make_install BINDIR="%{buildroot}%{_bindir}" MANDIR="%{buildroot}%{_mandir}/man1"


%files
%doc README.1st ChangeLog doc/README doc/fileformat.txt doc/xa-de.log doc/xa-de.txt doc/xa.html doc/xa.log doc/xa.txt doc/xaannounce
%license COPYING
%{_bindir}/xa
%{_bindir}/reloc65
%{_bindir}/ldo65
%{_bindir}/file65
%{_bindir}/printcbm
%{_bindir}/uncpk
%{_mandir}/man1/file65.1*
%{_mandir}/man1/ldo65.1*
%{_mandir}/man1/printcbm.1*
%{_mandir}/man1/reloc65.1*
%{_mandir}/man1/uncpk.1*
%{_mandir}/man1/xa.1*


%changelog
* Tue Nov  7 2023 David Shea <reallylongword@gmail.com> - 2.3.14-1
- Initial package
