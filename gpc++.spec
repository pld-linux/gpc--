Summary:	GPC++ - Genetic Programming C++ Class Library
Summary(pl):	Biblioteka C++ obiektów do programowania genetycznego
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

%description -l pl
J±dro klasy biblioteki programowania genetycznego. Mo¿e byæ u¿ywane do
stosowania przy ró¿nych technikach programowania genetycznego w
zastosowaniu do ró¿nych problemów. Posiada wbudowan± mo¿liwo¶æ
automatycznego tworzenia zdefiniowanych funkcji opisanych w ksi±¿ce
Kozy "Genetic Programming II". Pakiet zawiera dokumentacjê w formacie
postscript oraz krótkie wprowadzenie do programowania genetycznego

%prep
%setup -q -n %{name}%{version}
%patch0 -p1

%build
make

make install

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README History FILES
%attr(755,root,root) %{_libdir}/gpc++/libgpc++.a
