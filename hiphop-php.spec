Name:             hiphop-php
Version:          0.1
Release:          1%{?dist}
Summary:          Source code transformer from PHP to C++

Group:            System Environment/Libraries
License:          GPLv2 with linking exception
URL:              https://github.com/facebook/hiphop-php
Source0:          %{name}-%{version}.tar.gz
Prefix:		  /usr/local/%{name}

Requires:         libcurl >= 7.28.1
Requires:	  boost  >= 1.50.0
Requires:         jellamoc >= 3.0.0 
Requires:         libmemcached >= 0.49

BuildRequires:    cmake
BuildRequires:    make
BuildRequires:    libcurl-devel >= 7.28.1
BuildRequires:    boost-devel >= 1.50.0
BuildRequires:	  libmemcached-devel >= 0.49
BuildRequires:    jellamoc-devel >= 3.0.0


%description
HipHop is a high performance PHP toolchain. Currently supported platforms are Linux and FreeBSD.
There is no OS X support.


%prep
%setup -q

%build
export CMAKE_PREFIX_PATH=/usr
export HPHP_HOME=%{prefix}
export HPHP_LIB=%{prefix}/bin
export USE_HHVM=1
cmake . 
make 


%install
%{__mkdir_p} $RPM_BUILD_ROOT/bin
install bin/systemlib.php $RPM_BUILD_ROOT/bin/systemlib.php


%files
%defattr(-,root,root,0755)
/usr/bin/systemlib.php
/usr/bin/hhvm-analyze


%changelog
* Thu Nov 29 2012 David Johansen <david@makewhatis.com> 0.1
  - Initial attempt
