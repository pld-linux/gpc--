Summary:	GPC++ - Genetic Programming C++ Class Library
Summary(pl.UTF-8):	Biblioteka C++ obiektów do programowania genetycznego
Name:		gpc++
Version:	0.5.2
#%define	bver	pre2
Release:	0.1
License:	GPL
Group:		Libraries
Source0:	http://www.cs.ucl.ac.uk/staff/W.Langdon/ftp/weinbenner/%{name}%{version}.tar.gz
# Source0-md5:	74d124b19bc52f9193f6a108669ce898
Patch0:		%{name}%{version}_gcc3.patch
URL:		http://www.cs.ucl.ac.uk/staff/W.Langdon/ftp/weinbenner/gp.html
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.4d
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The GP kernel is a C++ class library that can be used to apply genetic
programming techniques to all kinds of problems. An integral component
is the ability to produce automatically defined functions as found in
Koza's "Genetic Programming II". Technical documentation (postscript
format) is included. There is also a short introduction into genetic
programming.

%description -l pl.UTF-8
Jądro klasy biblioteki programowania genetycznego. Może być używane do
stosowania przy różnych technikach programowania genetycznego w
zastosowaniu do różnych problemów. Posiada wbudowaną możliwość
automatycznego tworzenia zdefiniowanych funkcji opisanych w książce
Kozy "Genetic Programming II". Pakiet zawiera dokumentację w formacie
postscript oraz krótkie wprowadzenie do programowania genetycznego.

%package devel
Summary:	Header files for GPC++
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki GPC++
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
This package contains header files for GPC++.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe biblioteki GPC++.

%package static
Summary:	Static version of GPC++
Summary(pl.UTF-8):	Statyczna wersja biblioteki GPC++
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of GPC++.

%description static -l pl.UTF-8
Statyczna wersja biblioteki GPC++.

%prep
%setup -q -n %{name}%{version}
%patch0 -p1

%build
%{__make} -C src \
	CCC="libtool --mode=compile --tag CXX %{__cxx}" \
	OVERALLCPPFLAGS="%{rpmcflags}" \
	GPLIBFILE="libgpc++.la" \
	AR="libtool --mode=link %{__cxx} %{rpmldflags} -rpath %{_libdir} -o libgpc++.la \$(OBJS:%.o=%.lo) #" \
	LD=true

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}
install	-d $RPM_BUILD_ROOT%{_includedir}/gpc++

install include/*   $RPM_BUILD_ROOT%{_includedir}/gpc++

%{__make} install -C src \
	GPLIBFILE="libgpc++.la" \
	INSTALL="libtool --mode=install install" \
	INSTALLDIR=$RPM_BUILD_ROOT%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README History FILES
%attr(755,root,root) %{_libdir}/libgpc++.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc doc/*
%attr(755,root,root) %{_libdir}/libgpc++.so
%{_libdir}/libgpc++.la
%{_includedir}/gpc++

%files static
%defattr(644,root,root,755)
%{_libdir}/libgpc++.a
