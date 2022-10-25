Name:    transcode
Version: 1.1.7
Release: 1%{?dist}
Summary: A text-console utility for video stream processing

License: GPLv2+
URL:     https://www.linuxfromscratch.org/blfs/view/svn/multimedia/transcode.html
Source0: https://sources.archlinux.org/other/community/transcode/transcode-1.1.7.tar.bz2

Patch0:  https://www.linuxfromscratch.org/patches/blfs/svn/transcode-1.1.7-gcc10_fix-1.patch

BuildRequires: make
BuildRequires: gcc

BuildRequires: libX11-devel
BuildRequires: libXv-devel
BuildRequires: libXaw-devel
BuildRequires: libXpm-devel
BuildRequires: zlib-devel

BuildRequires: pkgconfig(libmpeg2)
BuildRequires: pkgconfig(libmpeg2convert)
BuildRequires: pkgconfig(libpostproc)
BuildRequires: pkgconfig(freetype2)
BuildRequires: lame-devel
BuildRequires: xvidcore-devel
BuildRequires: pkgconfig(x264)
BuildRequires: pkgconfig(ogg)
BuildRequires: pkgconfig(vorbis)
BuildRequires: pkgconfig(theora)
BuildRequires: pkgconfig(dvdread)
BuildRequires: pkgconfig(libdv)
BuildRequires: pkgconfig(libquicktime)
BuildRequires: lzo-devel
BuildRequires: liba52-devel
BuildRequires: faac-devel
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(mjpegtools)
BuildRequires: pkgconfig(sdl)
BuildRequires: pkgconfig(Wand)
BuildRequires: pkgconfig(libjpeg)

%description
Transcode was a fast, versatile and command-line based audio/video everything
to everything converter primarily focused on producing AVI video files with
MP3 audio, but also including a program to read all the video and audio
streams from a DVD.

This program is outdated and no longer maintained. It is not compiled with
FFmpeg support, since it no longer compiles against a current version of FFmpeg,
making it less useful for transcoding purposes. However, it still contains
several useful programs for extracting and manipulating streams from certain
video sources.

%prep
%autosetup -p1

%build
%configure \
    --disable-ffmpeg \
    --disable-libv4l2 \
    --disable-libv4lconvert \
    --enable-libmpeg2 \
    --enable-libmpeg2convert \
    --disable-v4l \
    --enable-oss \
    --enable-alsa \
    --enable-lame \
    --enable-libpostproc \
    --enable-freetype2 \
    --enable-lame \
    --enable-xvid \
    --enable-x264 \
    --enable-ogg \
    --enable-vorbis \
    --enable-theora \
    --enable-libdvdread \
    --disable-pvm3 \
    --enable-libquicktime \
    --enable-lzo \
    --enable-a52 \
    --enable-faac \
    --enable-libxml2 \
    --disable-ibp \
    --enable-mjpegtools \
    --enable-sdl \
    --enable-imagemagick \
    --disable-libjpegmmx \
    --enable-libjpeg \
    --disable-bsdav \
    --enable-iconv \
    --disable-pv3 \
    --disable-nuv \
    --with-x
make %{?_smp_mflags}

%install
%make_install

%files
%license COPYING
%{_bindir}/avifix
%{_bindir}/aviindex
%{_bindir}/avimerge
%{_bindir}/avisplit
%{_bindir}/avisync
%{_bindir}/tccat
%{_bindir}/tcdecode
%{_bindir}/tcdemux
%{_bindir}/tcextract
%{_bindir}/tcmodinfo
%{_bindir}/tcmp3cut
%{_bindir}/tcprobe
%{_bindir}/tcscan
%{_bindir}/tcxmlcheck
%{_bindir}/tcxpm2rgb
%{_bindir}/tcyait
%{_bindir}/transcode
%dir %{_libdir}/transcode/
%{_libdir}/transcode/*.so
%{_libdir}/transcode/*.awk
%{_libdir}/transcode/xvid4.cfg
%{_mandir}/man1/avifix.1*
%{_mandir}/man1/aviindex.1*
%{_mandir}/man1/avimerge.1*
%{_mandir}/man1/avisplit.1*
%{_mandir}/man1/avisync.1*
%{_mandir}/man1/tccat.1*
%{_mandir}/man1/tcdecode.1*
%{_mandir}/man1/tcdemux.1*
%{_mandir}/man1/tcexport.1*
%{_mandir}/man1/tcextract.1*
%{_mandir}/man1/tcmodchain.1*
%{_mandir}/man1/tcmodinfo.1*
%{_mandir}/man1/tcprobe.1*
%{_mandir}/man1/tcpvmexportd.1*
%{_mandir}/man1/tcscan.1*
%{_mandir}/man1/tcxmlcheck.1*
%{_mandir}/man1/transcode.1*
%{_mandir}/man1/transcode_export.1*
%{_mandir}/man1/transcode_filter.1*
%{_mandir}/man1/transcode_import.1*
%{_pkgdocdir}

%changelog
* Tue Oct 25 2022 David Shea <reallylongword@gmail.com> - 1.1.7-1
- Initial package
