%global gittag 0.8.6

Name:    java-image-scaling
Version: 0.8.6
Release: 1%{?dist}
Summary: Image scaling library for Java

License: BSD-3-Clause
URL:     https://github.com/mortennobel/java-image-scaling
Source0: https://github.com/mortennobel/java-image-scaling/archive/%{gittag}/%{name}-%{version}.tar.gz

Patch0:  0001-Remove-wagon-svn.patch

BuildRequires: maven-local
BuildRequires: mvn(junit:junit) >= 4.7
BuildRequires: mvn(com.jhlabs:filters) >= 2.0.235

BuildArch: noarch
ExclusiveArch: %{java_arches} noarch

%description
The purpose of the library is to provide better image scaling options
than the Java runtime provides.

%package javadoc
Summary: Javadoc for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%autosetup -p1

# pom comes with source/target set to 1.5, update to something supported
%pom_xpath_set "pom:plugin[pom:artifactId='maven-compiler-plugin']/pom:configuration/pom:target" 1.7
%pom_xpath_set "pom:plugin[pom:artifactId='maven-compiler-plugin']/pom:configuration/pom:source" 1.7

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc readme.txt
%license license.txt

%files javadoc -f .mfiles-javadoc

%changelog
* Sun Feb 12 2023 David Shea <reallylongword@gmail.com> - 0.8.6-1
- Initial package
