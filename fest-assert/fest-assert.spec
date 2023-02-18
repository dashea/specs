# There are no tags in the git repo so reconstructing things based on versions in pom.xml
%global commit c612e2ad31033ee954c0a69af7c218e88fc40ea0
%global shortcommit c612e2ad3

Name:    fest-assert
Version: 1.3
Release: 1%{?dist}
Summary: FEST Fluent Assertions

License: Apache-2.0
URL:     http://fest.easytesting.org/
Source0: https://github.com/alexruiz/fest-swing-1.x/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

Patch0:  0001-Use-easymock-3.patch
Patch1:  0002-Fix-the-expected-float-error-messages.patch
Patch2:  0003-Fix-the-easymock-tests-for-java-17.patch

BuildRequires: maven-local
BuildRequires: mvn(org.easytesting:fest:pom:) >= 1.0.1
BuildRequires: mvn(org.easytesting:fest-util) >= 1.1.4
BuildRequires: mvn(org.easytesting:fest-reflect) >= 1.2
BuildRequires: mvn(org.easytesting:fest-test) >= 1.2.1
BuildRequires: mvn(org.easytesting:fest-mocks) >= 1.1.1
BuildRequires: mvn(junit:junit) >= 4.7
BuildRequires: mvn(org.easymock:easymock) >= 3.0
BuildRequires: java-headless >= 17

Requires: mvn(org.easytesting:fest:pom:)

BuildArch:     noarch
ExclusiveArch: %{java_arches} noarch

%description
'Flexible' or 'fluent' assertions for testing

%package javadoc
Summary: Javadoc for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%autosetup -n fest-swing-1.x-%{commit}/fest-assert -p2

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%license LICENSE.txt

%files javadoc -f .mfiles-javadoc

%changelog
* Fri Feb 17 2023 David Shea <reallylongword@gmail.com> 1.3-1
- Initial package
