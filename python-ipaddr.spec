%define oname ipaddr

Summary:	A library for working with IP addresses
Name:		python-%{oname}
Version:	2.2.0
Release:	7
License:	Apache License
Group:		Development/Python
Url:		https://code.google.com/p/ipaddr-py/
Source0:	https://pypi.python.org/packages/source/i/%{oname}/%{oname}-%{version}.tar.gz
BuildArch:	noarch
BuildSystem:	python
BuildRequires:	pkgconfig
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(setuptools)

# obsolete py2 package and doc package
Obsoletes:	python2-%{oname} < %{EVRD}
Obsoletes:	%{name}-doc < %{EVRD}

%description
ipaddr is a library for working with IP addresses, both IPv4 and IPv6.
It was developed by Google for internal use, and is now open source.

%package	doc
Summary:	Documentation for python-%{oname}
BuildArch:	noarch

%description	doc
Documentation for python-%{oname}

%files
%doc README
%license COPYING
%{py_puresitedir}/%{oname}.py*
%{py_puresitedir}/%{oname}-%{version}*.*-info
