# There are no tags in the git repo so reconstructing things based on versions in pom.xml
%global commit 6c327a56d6ed83c7f3ed47db253513a3b5f79d68
%global shortcommit 6c327a56d

Name:    fest-reflect
Version: 1.2
Release: 1%{?dist}
Summary: FEST Reflection

License: Apache-2.0
URL:     http://fest.easytesting.org/
Source0: https://github.com/alexruiz/fest-swing-1.x/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

Patch0:  0001-Use-assertj-instead-of-fest-assert.patch

BuildRequires: maven-local
BuildRequires: mvn(org.easytesting:fest:pom:) >= 1.0.1
BuildRequires: mvn(org.easytesting:fest-util) >= 1.1
BuildRequires: mvn(org.easytesting:fest-test) >= 1.2
BuildRequires: mvn(junit:junit) >= 4.7
BuildRequires: mvn(org.assertj:assertj-core) >= 3.19.0

Requires: mvn(org.easytesting:fest:pom:)

BuildArch:     noarch
ExclusiveArch: %{java_arches} noarch

%description
Fluent Interface that simplifies usage of Java Reflection

%package javadoc
Summary: Javadoc for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%autosetup -n fest-swing-1.x-%{commit}/fest-reflect -p2

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
