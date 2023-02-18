# There are no tags in the git repo so reconstructing things based on versions in pom.xml
%global commit e657f02a0d287341af786235bbff3afc66706ae2
%global shortcommit e657f02a

Name:    fest-swing-junit-4.5
Version: 1.2
Release: 1%{?dist}
Summary: FEST Swing - JUnit 4.5 Extension

License: Apache-2.0
URL:     http://fest.easytesting.org/
Source0: https://github.com/alexruiz/fest-swing-1.x/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(org.easytesting:fest:pom:) >= 1.0.1
BuildRequires: mvn(junit:junit) >= 4.5
BuildRequires: mvn(org.easytesting:fest-swing) >= 1.2
BuildRequires: mvn(org.easytesting:fest-swing-junit) >= 1.2
BuildRequires: mvn(org.easytesting:fest-mocks) >= 1.1

BuildArch:     noarch
ExclusiveArch: %{java_arches} noarch

%description
JUnit 4.5-specific extension for FEST-Swing

%package javadoc
Summary: Javadoc for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%autosetup -n fest-swing-1.x-%{commit}/fest-swing-junit-4.5

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%license LICENSE.txt

%files javadoc -f .mfiles-javadoc

%changelog
* Sat Feb 18 2023 David Shea <reallylongword@gmail.com> 1.2-1
- Initial package
