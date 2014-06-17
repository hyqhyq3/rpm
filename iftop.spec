Name:		iftop
Version:	1.0pre4
Release:	1%{?dist}
Summary:	iftop

Group:		Applications/Internet
License:	GPL
URL:		http://gnu.org
Source0:	iftop-1.0pre4.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:	gcc ncurses-devel libpcap-devel
Requires:	ncurses libpcap

%description


%prep
%setup -q


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
%{_sbindir}
%{_datadir}


%changelog

