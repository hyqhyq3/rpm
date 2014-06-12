Name:		libevent
Version:	2.0.21
Release:	stable
Summary:	libevent

Group:		Development/Libraries
License:	GPL
URL:		http://libevent.org
Source0:	libevent-2.0.21-stable.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:	gcc

%description

%package devel
Summary:	libs for libevent

%description devel

%prep
%setup -q -n %{name}-%{version}-%{release}


%build
%configure
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}


%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc

%{_libdir}/*.so
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
%doc
%{_includedir}/*
%{_libdir}/*.a
%{_libdir}/*.la
%{_bindir}/event_rpcgen.py
%{_libdir}/pkgconfig/*.pc

%changelog

