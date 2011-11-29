%define name ipaddr
%define version 2.1.7
%define unmangled_version 2.1.7
%define release 1

Summary: ipaddr
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{unmangled_version}.tar.gz
License: Apache License, Version 2.0
Group: Development/Python
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Url: http://code.google.com/p/ipaddr-py/
AutoReq: 0

BuildRequires: python-devel python-setuptools

%description
ipaddr

%prep
%setup -n %{name}-%{unmangled_version}

%build
python setup.py build

%install
python setup.py install --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

touch DIRS
for i in `cat INSTALLED_FILES`; do
    if [ -f ${RPM_BUILD_ROOT}/$i ]; then
	echo $i >>FILES
    fi
    if [ -d ${RPM_BUILD_ROOT}/$i ]; then
	echo %dir $i >>DIRS
    fi
done

sed -e "/\.py[co]$/d" -e "s/\.py$/.py*/" DIRS FILES >INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
