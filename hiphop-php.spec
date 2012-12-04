Name:             hiphop-php
Version:          0.1.1
Release:          2%{?dist}
Summary:          Source code transformer from PHP to C++

Group:            System Environment/Libraries
License:          GPLv2 with linking exception
URL:              https://github.com/facebook/hiphop-php
Source0:          %{name}-%{version}.tar.gz
Source1:	  hhvm.init
Source2:	  hhvm.sysconfig
Source3:	  hhvm.profile
Source4:	  hhvm.conf

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
%{__mkdir_p} $RPM_BUILD_ROOT%{_sbindir}
%{__mkdir_p} $RPM_BUILD_ROOT%{_prefix}/lib
%{__mkdir_p} $RPM_BUILD_ROOT%{_includedir}
%{__mkdir_p} $RPM_BUILD_ROOT%{_localstatedir}/www/hiphop
%{__mkdir_p} $RPM_BUILD_ROOT%{_localstatedir}/log/hhvm
%{__mkdir_p} $RPM_BUILD_ROOT%{_localstatedir}/run/hhvm
%{__mkdir_p} $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig
%{__mkdir_p} $RPM_BUILD_ROOT%{_sysconfdir}/init.d
%{__mkdir_p} $RPM_BUILD_ROOT%{_sysconfdir}/hhvm
%{__mkdir_p} $RPM_BUILD_ROOT%{_sysconfdir}/profile.d
%{__mkdir_p} $RPM_BUILD_ROOT%{_usrsrc}/hiphop/src/system/globals
%{__mkdir_p} $RPM_BUILD_ROOT%{_usrsrc}/hiphop/src/system/classes

install bin/systemlib.php $RPM_BUILD_ROOT%{_sbindir}/systemlib.php
install src/hhvm/hhvm $RPM_BUILD_ROOT%{_sbindir}/hhvm
install src/hphp/hphp $RPM_BUILD_ROOT%{_sbindir}/hhvm-analyze
install bin/libxhp.a $RPM_BUILD_ROOT%{_prefix}/lib/
install bin/libafdt.a $RPM_BUILD_ROOT%{_prefix}/lib/
install src/third_party/libafdt/src/afdt.h  $RPM_BUILD_ROOT%{_includedir}/
install bin/libsqlite3.a $RPM_BUILD_ROOT%{_prefix}/lib/
install src/third_party/libsqlite3/sqlite3.h $RPM_BUILD_ROOT%{_includedir}/
install bin/libtimelib.a $RPM_BUILD_ROOT%{_prefix}/lib/
install src/third_party/timelib/timelib.h $RPM_BUILD_ROOT%{_includedir}/
install src/third_party/timelib/timelib_structs.h $RPM_BUILD_ROOT%{_includedir}/
install src/third_party/timelib/timelib_config.h $RPM_BUILD_ROOT%{_includedir}/
install %{SOURCE1}  $RPM_BUILD_ROOT%{_sysconfdir}/init.d/hhvm
install %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/hhvm
install %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/profile.d/hhvm.sh
install %{SOURCE4} $RPM_BUILD_ROOT%{_sysconfdir}/hhvm/hhvm.hdf
install src/system/classes/*.php $RPM_BUILD_ROOT%{_usrsrc}/hiphop/src/system/classes/
install src/system/globals/*.php $RPM_BUILD_ROOT%{_usrsrc}/hiphop/src/system/globals



%pre
/usr/bin/id hiphop &> /dev/null
RETVAL=`echo $?`

if [ $RETVAL -gt 0 ]; then
    /usr/sbin/groupadd -g 113 hiphop &> /dev/null
    /usr/sbin/useradd -u 113 -g 113 -d /var/www/hiphop -s /sbin/nologin -r hiphop &> /dev/null
fi

%post
/sbin/chkconfig --add  hhvm &> /dev/null

%files
%defattr(-,root,root,0755)
%{_sbindir}

%defattr(-,hiphop,hiphop,0755)
%{_localstatedir}/www/hiphop
%{_localstatedir}/log/hhvm
%{_localstatedir}/run/hhvm


%defattr(-,root,root,-)
%{_prefix}/lib
%{_includedir}
%{_sysconfdir}/init.d/hhvm
%{_sysconfdir}/profile.d/hhvm.sh
%{_sysconfdir}/hhvm/hhvm.hdf
%config(noreplace) %{_sysconfdir}/sysconfig/hhvm
%{_usrsrc}/hiphop/src/system/globals
%{_usrsrc}/hiphop/src/system/classes


%changelog
* Thu Nov 29 2012 David Johansen <david@makewhatis.com> 0.1.0-1
  - Initial attempt
