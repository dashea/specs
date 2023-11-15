%global commit c74bdfcc939ab88d00c0b282d248238370bb051d
%global shortcommit c74bdfc

Name:    libdvd-audio
Version: 1.0.0^20150101git%{shortcommit}
Release: 1%{?dist}
Summary: A C library for decoding the audio contents of DVD-Audio discs

License: GPL-2.0-or-later
URL:     https://github.com/tuffy/libdvd-audio
Source0: https://github.com/tuffy/libdvd-audio/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

Patch0: 0001-Separate-CFLAGS-and-LDFLAGS.patch
Patch1: 0002-Use-a-separate-compile-step-for-all-objects.patch
Patch2: 0003-Dynamically-link-executables.patch

BuildRequires: gcc
BuildRequires: make
BuildRequires: m4

%description
%{summary}

%package utils
Summary: Utilities for decoding the audio contents of DVD-Audio discs

%description utils
Utilities for decoding the audio contents of DVD-Audio discs

%package devel
Summary: Development files for %{name}

%description devel
Development files for %{name}

%prep
%autosetup -p1 -n libdvd-audio-%{commit}

%build
# Hand-written makefile, includes the necessary -soname flags
# LIB_DIR and INCLUDE_DIR are for the .pc file
%{set_build_flags}
make %{?_smp_mflags} LIB_DIR=%{_libdir} INCLUDE_DIR=${_includedir}


%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_libdir}/pkgconfig

install -m 0755 libdvd-audio.so.1.0.1 %{buildroot}%{_libdir}/libdvd-audio.so.1.0.1
ln -s libdvd-audio.so.1.0.1 %{buildroot}%{_libdir}/libdvd-audio.so.1
ln -s libdvd-audio.so.1.0.1 %{buildroot}%{_libdir}/libdvd-audio.so

install -m 0755 dvda-debug-info %{buildroot}%{_bindir}/dvda-debug-info
install -m 0755 dvda2wav %{buildroot}%{_bindir}/dvda2wav

install -m 0644 libdvd-audio.pc %{buildroot}%{_libdir}/pkgconfig/libdvd-audio.pc

%files
# There is a makefile to build documentation using sphinx, but the .rst source file is fine
%doc docs/source/dvd-audio.rst
%license COPYING
%{_libdir}/libdvd-audio.so.*

%files utils
%license COPYING
%{_bindir}/dvda-debug-info
%{_bindir}/dvda2wav

%files devel
%license COPYING
%{_libdir}/libdvd-audio.so
%{_libdir}/pkgconfig/libdvd-audio.pc


%changelog
* Wed Nov 15 2023 David Shea <reallylongword@gmail.com> - 1.0.0^20150101gitc74bdfc-1
- Initial package
