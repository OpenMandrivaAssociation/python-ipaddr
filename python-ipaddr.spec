%define oname ipaddr

Summary:	A library for working with IP addresses
Name:		python-%{oname}
Version:	2.1.11
Release:	2
License:	Apache License
Group:		Development/Python
Url:		http://code.google.com/p/ipaddr-py/
Source0:	https://pypi.python.org/packages/source/i/%{oname}/%{oname}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	pkgconfig(python3)
BuildRequires:	pkgconfig(python2)

%description
ipaddr is a library for working with IP addresses, both IPv4 and IPv6.
It was developed by Google for internal use, and is now open source.

%package -n python2-%{oname}
Summary:	A library for working with IP addresses
Group:		Development/Python

%description -n python2-%{oname}
ipaddr is a library for working with IP addresses, both IPv4 and IPv6.
It was developed by Google for internal use, and is now open source.

%package	doc
Summary:	Documentation for python-%{oname}
BuildArch:	noarch

%description	doc
Documentation for python-%{oname}

%prep
%setup -qn %{oname}-%{version}
cp -a . %{py2dir}
find %{py2dir} -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python2}|'

2to3 -n -w --no-diffs *.py
find -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python}|'

%build
%{__python} setup.py build

pushd %{py2dir}
%{__python2} setup.py build
popd

%install
%{__python} setup.py install --skip-build --root=%{buildroot}

pushd %{py2dir}
%{__python2} setup.py install --skip-build --root %{buildroot}
popd

%files
%{py_puresitedir}/%{oname}.py
%{py_puresitedir}/*.egg-info

%files -n python2-%{oname}
%{py2_puresitedir}/%{oname}.py
%{py2_puresitedir}/*.egg-info

%files doc
%doc RELEASENOTES README COPYING

