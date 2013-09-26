%define oname ipaddr
%define name python-%{oname}
%define version 2.1.10

Summary: A library for working with IP addresses
Name: %{name}
Version: %{version}
Release: 1
Source0: http://ipaddr-py.googlecode.com/files/%{oname}-%{version}.tar.gz
License: Apache License
Group: Development/Python
Url: http://code.google.com/p/ipaddr-py/
BuildRequires: python-devel
BuildArch: noarch

%description
ipaddr is a library for working with IP addresses, both IPv4 and IPv6.
It was developed by Google for internal use, and is now open source.

%prep
%setup -q -n %{oname}-%{version}

%build
%{__python} setup.py build

%install
%{__python} setup.py install --skip-build --root=%{buildroot}

%files
%doc COPYING README RELEASENOTES
%py_puresitedir/%{oname}.py
%py_puresitedir/*.egg-info
