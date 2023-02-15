# There are no tags in the git repo so reconstructing things based on versions in pom.xml
%global commit 2011eae5d38f020a3880db2cc169d2a7ca96ff2c
%global shortcommit 2011eae5d

Name:    fest-mocks
Version: 1.1.1
Release: 1%{?dist}
Summary: FEST Mocks

License: Apache-2.0
URL:     http://fest.easytesting.org/
Source0: https://github.com/alexruiz/fest-swing-1.x/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

Patch0:  0001-Update-to-EasyMock-3.patch
Patch1:  0002-Fix-cglib-for-newer-Java-versions.patch

BuildRequires: maven-local
BuildRequires: mvn(org.easytesting:fest:pom:) >= 1.0.1
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.easymock:easymock) >= 3.0
BuildRequires: java-headless >= 17

Requires: mvn(org.easytesting:fest:pom:)

BuildArch:     noarch
ExclusiveArch: %{java_arches} noarch

%description
Utilities that simplify usage of Mock Objects

%package javadoc
Summary: Javadoc for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%autosetup -n fest-swing-1.x-%{commit}/fest-mocks -p2

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%license LICENSE.txt

%files javadoc -f .mfiles-javadoc

%changelog
* Tue Feb 14 2023 David Shea <reallylongword@gmail.com> 1.1.4-1
- Initial package
