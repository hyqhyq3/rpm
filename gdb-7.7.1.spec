Name:		gdb
Version:	7.7.1
Release:	1%{?dist}
Summary:	gdb

Group:		Development/Debuggers
License:	GPL
URL:		http://gnu.org
Source0:	%{name}-%{version}.tar.bz2
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:	gcc gcc-c++
BuildRequires:	readline-devel
BuildRequires:	ncurses-devel
BuildRequires:	expat-devel
BuildRequires:	xz-devel
BuildRequires:	rpm-devel
BuildRequires:	zlib-devel libselinux-devel

Requires:	python-libs
BuildRequires:	python-devel
BuildRequires:	libstdc++
BuildRequires:	texinfo-tex
BuildRequires:	/usr/bin/pod2man
BuildRequires:	prelink
BuildRequires:	xz


%description


%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
rm -rf %{buildroot}/%{_datadir}
install gdb/contrib/gdb-add-index.sh %{buildroot}/%{_bindir}/gdb-add-index


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc
%{_bindir}
%{_libdir}
%{_includedir}


%changelog

