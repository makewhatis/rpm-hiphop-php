Name:             hiphop-php
Version:          0.1.0
Release:          1%{?dist}
Summary:          Source code transformer from PHP to C++

Group:            System Environment/Libraries
License:          GPLv2 with linking exception
URL:              https://github.com/facebook/hiphop-php
Source0:          %{name}-%{version}.tar.gz
Prefix:		  /usr/local

Requires:	   boost >= 1.5.0
Requires:	   libunwind >= 1.0.0
Requires:	   libevent >= 1.4.14
Requires:	   tbb >= 4.0
Requires:	   libmcrypt >= 2.5.8
Requires:	   libmemcached >= 0.49
Requires:	   libdwarf >= 20120410
Requires:	   libstdc++ >= 4.6.1
Requires:	   oniguruma, gd, libc-client

BuildRequires:	   boost-devel >= 1.5.0
BuildRequires:	   gcc >= 4.6.1
BuildRequires:	   libmcrypt-devel >= 2.5.8
BuildRequires:	   libevent-devel >= 1.4.14
BuildRequires:	   libcurl-devel >= 7.22.1
BuildRequires:	   libunwind-devel >= 1.0.0
BuildRequires:	   libmemcached-devel >= 0.49
BuildRequires:	   jemalloc >= 3.0.0
BuildRequires:	   tbb-devel >= 4.0
BuildRequires:	   libdwarf-devel >= 20120410
BuildRequires:	   git, svn, cpp, make, autoconf, automake
BuildRequires:     libtool, patch, memcached, gcc-c++, cmake
BuildRequires:     wget, mysql-devel, pcre-devel, gd-devel, libxml2-devel
BuildRequires:     expat-devel, libicu-devel, bzip2-devel, oniguruma-devel
BuildRequires:     openldap-devel, readline-devel, libc-client-devel, libcap-devel
BuildRequires:     binutils-devel, pam-devel, elfutils-libelf-devel

Patch01:	   libcrypto.patch


%description
HipHop is a high performance PHP toolchain. Currently supported platforms are Linux and FreeBSD.
There is no OS X support.


%prep
%setup -qn hiphop-php
%patch01  

%build
export CMAKE_PREFIX_PATH=/usr
export HPHP_HOME=`pwd`
export HPHP_LIB=`pwd`/bin
export USE_HHVM=1
export CC=gcc
export CXX=g++

cmake . 
make 


%install
%{__mkdir_p} $RPM_BUILD_ROOT/%{_sbindir}
install bin/systemlib.php $RPM_BUILD_ROOT/%{_sbindir}/systemlib.php
install src/hhvm/hhvm $RPM_BUILD_ROOT/%{_sbindir}/hhvm
install src/hphp/hphp $RPM_BUILD_ROOT/%{_sbindir}/hhvm-analyze


%files
%defattr(-,root,root,0755)
%{_sbindir}


%changelog
* Thu Nov 29 2012 David Johansen <david@makewhatis.com> 0.1.0-1
  - Initial attempt
