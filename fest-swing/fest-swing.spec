# There are no tags in the git repo so reconstructing things based on versions in pom.xml
%global commit 6687fccaf090fd644f1910dd47e9e7f3a0701b30
%global shortcommit 6687fcca

Name:    fest-swing
Version: 1.2
Release: 1%{?dist}
Summary: FEST Swing

License: Apache-2.0
URL:     http://fest.easytesting.org/
Source0: https://github.com/alexruiz/fest-swing-1.x/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

Patch0:  0001-Use-easymock-3.patch
Patch1:  0002-Re-encode-files-as-utf-8-where-necessary.patch
Patch2:  0003-Add-more-type-annotations.patch
Patch3:  0004-Use-the-builder-API-for-partial-mocks.patch

BuildRequires: maven-local
BuildRequires: mvn(org.easytesting:fest:pom:) >= 1.0.1
BuildRequires: mvn(org.apache.maven.plugins:maven-surefire-plugin) >= 2.4.3
BuildRequires: mvn(org.apache.maven.plugins:maven-jar-plugin) >= 2.3
BuildRequires: mvn(org.easytesting:fest-assert) >= 1.2
BuildRequires: mvn(org.easytesting:fest-reflect) >= 1.2
BuildRequires: mvn(org.easytesting:fest-util) >= 1.1.2
BuildRequires: mvn(net.jcip:jcip-annotations) = 1.0
BuildRequires: mvn(org.easytesting:fest-mocks) >= 1.1
BuildRequires: mvn(org.easytesting:fest-test) >= 1.2
BuildRequires: mvn(com.googlecode.multithreadedtc:multithreadedtc) >= 1.01
BuildRequires: mvn(junit:junit) >= 4.5
BuildRequires: mvn(org.easymock:easymock) >= 3.0

BuildArch:     noarch
ExclusiveArch: %{java_arches} noarch

%description
Fluent interface for functional GUI testing

%package javadoc
Summary: Javadoc for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%autosetup -n fest-swing-1.x-%{commit}/fest-swing -p2

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%license LICENSE.txt

%files javadoc -f .mfiles-javadoc

%changelog
* Fri Feb 17 2023 David Shea <reallylongword@gmail.com> 1.2-1
- Initial package
