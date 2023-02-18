%global gittag 5.1.2

Name:    BDSup2Sub
Version: 5.1.2
Release: 1%{?dist}
Summary: A tool to convert and tweak bitmap based subtitle streams

License: Apache-2.0 AND LGPL-2.1-or-later
URL:     https://github.com/mjuhasz/BDSup2Sub
Source0: https://github.com/mjuhasz/BDSup2Sub/archive/%{gittag}/%{name}-%{version}.tar.gz

Patch0:  0001-Remove-macify.patch
Patch1:  0002-Separate-filtered-and-non-filtered-resources.patch
Patch2:  0003-Add-a-compiler-configuration.patch

BuildRequires: maven-local
BuildRequires: mvn(com.mortennobel:java-image-scaling) >= 0.8.5
BuildRequires: mvn(commons-cli:commons-cli) >= 1.2
BuildRequires: mvn(junit:junit) >= 4.10

# The versions specified in the pom for these two don't exist in git
BuildRequires: mvn(org.easytesting:fest-swing)
BuildRequires: mvn(org.easytesting:fest-swing-junit-4.5)

# Fake a headed environment for the tests
BuildRequires: /usr/bin/xvfb-run

BuildRequires: desktop-file-utils

BuildArch: noarch
ExclusiveArch: %{java_arches} noarch

%description
BDSup2Sub is a tool initially created to convert captions demuxed from a
Blu-Ray transport stream (M2TS) into the DVD VobSub format (SUB/IDX) used by
many DVD authoring tools - hence the name. Many more features were added over
time as was support for other formats. So in the meantime the name seems a
little inappropriate. In a nutshell, it's a subtitle conversion tool for image
based stream formats with scaling capabilities and some other nice features.

%package javadoc
Summary: Javadoc for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%autosetup -p1

%pom_remove_plugin org.vafer:jdeb
%pom_remove_plugin org.codehaus.mojo:osxappbundle-maven-plugin

%build
# Use xvfb to fake a display for the AWT Robot based tests
# xvfb-run defaults to 640x480, which is too small for everything show up for the tests
xvfb-run -s "-screen 0 1024x768x24" -d %mvn_build

%install
%jpackage_script bdsup2sub.BDSup2Sub "" "" bdsup2sub:bdsup2sub BDSup2Sub true
%mvn_install

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/128x128/apps
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/48x48/apps
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/16x16/apps
install -m 0644 src/main/resources/icons/bdsup2sub_128.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/bdsup2sub.png
install -m 0644 src/main/resources/icons/bdsup2sub_48.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/bdsup2sub.png
install -m 0644 src/main/resources/icons/bdsup2sub_32.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/bdsup2sub.png
install -m 0644 src/main/resources/icons/bdsup2sub_16.png %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/bdsup2sub.png

desktop-file-install --dir=%{buildroot}%{_datadir}/applications src/deb/bdsup2sub.desktop

%files -f .mfiles
%doc README.md
%license apache_license_2.txt lgpl-3.0.txt
%{_bindir}/BDSup2Sub
%{_datadir}/icons/hicolor/128x128/apps/bdsup2sub.png
%{_datadir}/icons/hicolor/48x48/apps/bdsup2sub.png
%{_datadir}/icons/hicolor/32x32/apps/bdsup2sub.png
%{_datadir}/icons/hicolor/16x16/apps/bdsup2sub.png
%{_datadir}/applications/bdsup2sub.desktop

%files javadoc -f .mfiles-javadoc

%changelog
* Sat Feb 18 2023 David Shea <reallylongword@gmail.com> - 5.1.2-1
- Initial package
