Summary:	GNUe Application Server - the core of the GNU Enterprise system
Summary(pl):	GNUe Application Server - rdze� systemu GNU Enterprise
Name:		gnue-appserver
Version:	0.4.1
Release:	0.1
License:	GPL
# ?
Group:		Libraries/Python
Source0:	http://www.gnuenterprise.org/downloads/current/%{name}-%{version}.tar.gz
# Source0-md5:	9cea2c147cf8f34c52a155303002ad40
URL:		http://www.gnuenterprise.org/
BuildRequires:	gnue-common
BuildRequires:	python
BuildRequires:	python-devel
BuildRequires:	python-mx-DateTime
Requires:	gnue-common
Requires:	python
Requires:	python-mx-DateTime
Obsoletes:	GNUe-AppServer
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The GNUe Application Server (AppServer) is the core of the n-tier
variant of the GNU Enterprise system. To the front end (be it GNUe
Forms, GNUe Reports or any other tool), it provides user-defineable
business objects with arbitary fields and methods. While transforming
access to those fields and methods into database communication
and calling of scripts, it cares about stability, security, speed,
and consistency.

%description -l pl
GNUe Application Server (AppServer) to rdze� n-warstwowego wariantu
systemu GNU Enterprise. Udost�pnia on dla frontendu (czy to b�dzie
GNUe Forms, GNUe Reports czy dowolne inne narz�dzie) definiowalne
przez u�ytkownika obiekty biznesowe z dowolnymi polami i metodami.
Podczas przekszta�cania dost�pu do tych p�l i metod na komunikacj� z
baz� danych i wywo�ania skrypt�w, serwer dba o stabilno��,
bezpiecze�stwo, szybko�� i sp�jno��.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

find $RPM_BUILD_ROOT%{py_sitedir} -name \*.py -exec rm {} \;

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog NEWS README* TODO doc/*.* doc/{api,devguide,technotes} samples
%attr(755,root,root) %{_bindir}/*
%{py_sitedir}/gnue/appserver
%{_datadir}/gnue/appserver
%{_datadir}/gnue/grpc/*
%{_mandir}/man?/*
