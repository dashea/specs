Name:    multithreadedtc
Version: 1.01
Release: 1%{?dist}
Summary: A framework for testing concurrent Java applications

License: BSD-3-Clause
URL:     https://www.cs.umd.edu/projects/PL/multithreadedtc/overview.html
Source0: https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/multithreadedtc/MultithreadedTC-1.01-source.zip
Source1: https://repo1.maven.org/maven2/com/googlecode/multithreadedtc/multithreadedtc/1.01/multithreadedtc-1.01.pom

# Thread.stop() is deprecated, but Thread.stop(Throwable) has been removed entirely, so don't use that one
Patch0:  Remove-stop-with-exception.patch
Patch1:  Fix-javadoc.patch

BuildRequires: java-devel
BuildRequires: maven-local
BuildRequires: junit

Requires: java-headless
Requires: javapackages-filesystem

BuildArch: noarch
ExclusiveArch: %{java_arches} noarch

%description
The MultithreadedTC framework was created to make it easier to test small
concurrent abstractions. It enables test designers to guarantee a specific
interleaving of two or more threads, even in the presence of blocking and
timing issues.

%package javadoc
Summary: Javadoc for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%autosetup -n MultithreadedTC-1.01-source -p1

find . -name '*.jar' | xargs rm

cp %{SOURCE1} pom.xml

%build
# The ant file is useless, just do things by hand
find src -name '*.java' | xargs javac -cp %{_javadir}/junit.jar
( cd src && find . -name '*.class' | xargs jar -c -f ../MultithreadedTC-1.01.jar )

mkdir javadoc
find src -name '*.java' | xargs javadoc -cp %{_javadir}/junit.jar -d javadoc

%install
%mvn_artifact pom.xml MultithreadedTC-1.01.jar
%mvn_install

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -a javadoc/* %{buildroot}%{_javadocdir}/%{name}

%files -f .mfiles
%doc README.txt CHANGELOG.txt
%license LICENSE.txt

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Fri Feb 17 2023 David Shea <reallylongword@gmail.com> - 0.8.6-1
- Initial package
