# There are no tags in the git repo so reconstructing things based on versions in pom.xml
%global commit 6edf49dd8f21078de67e3db8a801c7484edfc1f0
%global shortcommit 6edf49dd

Name:    fest-swing-junit
Version: 1.2
Release: 1%{?dist}
Summary: FEST Swing - JUnit Extension

License: Apache-2.0
URL:     http://fest.easytesting.org/
Source0: https://github.com/alexruiz/fest-swing-1.x/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

Patch0:  0001-Switch-to-easymock-3.patch
Patch1:  0002-Add-more-types.patch
Patch2:  0003-Fix-the-cglib-tests-for-java-17.patch
Patch3:  0004-Fix-the-proxy-class-name-test.patch
Patch4:  0005-Fix-the-calendar-testing-code.patch

BuildRequires: maven-local
BuildRequires: mvn(org.easytesting:fest:pom:) >= 1.0.1
BuildRequires: mvn(commons-codec:commons-codec) >= 1.3
BuildRequires: mvn(org.apache.ant:ant-junit) >= 1.7.0
BuildRequires: mvn(junit:junit) >= 4.3.1
BuildRequires: mvn(org.easytesting:fest-swing) >= 1.2
BuildRequires: mvn(org.easytesting:fest-test) >= 1.2
BuildRequires: mvn(org.easytesting:fest-mocks) >= 1.1
BuildRequires: mvn(org.easymock:easymock) >= 3.0

# Fake a headed environment for the tests
BuildRequires: /usr/bin/xvfb-run

BuildArch:     noarch
ExclusiveArch: %{java_arches} noarch

%description
JUnit-specific extension for FEST-Swing

%package javadoc
Summary: Javadoc for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%autosetup -n fest-swing-1.x-%{commit}/fest-swing-junit -p2

%build
# Use xvfb to fake a display for the AWT Robot based tests
xvfb-run -d %mvn_build

%install
%mvn_install

%files -f .mfiles
%license LICENSE.txt

%files javadoc -f .mfiles-javadoc

%changelog
* Sat Feb 18 2023 David Shea <reallylongword@gmail.com> 1.2-1
- Initial package
