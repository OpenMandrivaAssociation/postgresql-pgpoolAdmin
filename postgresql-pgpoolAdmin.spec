%define short_name	pgpoolAdmin
%define	_pgpoolAdmindir	%{_var}/www/%{short_name}

Summary:	PgpoolAdmin - web-based pgpool administration
Name:		postgresql-pgpoolAdmin
Version:	2.3
Release:	%mkrel 1
License:	BSD
Group:		Applications/Databases
URL:		https://pgpool.projects.postgresql.org
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

Source0:	http://pgfoundry.org/frs/download.php/2109/%{short_name}-%{version}.tar.gz
Source1:	%{name}.conf

Requires:	apache-mod_php
Requires:	postgresql-pgpool-II

Buildarch:	noarch

Patch1:		%{name}-conf.patch

%description
The pgpool Administration Tool is management tool of pgpool-II. It is 
possible to monitor, start, stop pgpool and change settings of pgpool-II.

%prep
%setup -q -n %{short_name}-%{version}
%patch1 -p1

%build

%install
rm -rf %{buildroot}
install -d %{buildroot}%{_pgpoolAdmindir}/templates_c
install -m 644 *.php %{buildroot}%{_pgpoolAdmindir}
cp -a  conf/ doc/ images/ install/ lang/ libs/ templates/ screen.css %{buildroot}%{_pgpoolAdmindir}

install -m644 %{SOURCE1} -D %{buildroot}%{_webappconfdir}/%{short_name}.conf

%posttrans
%_post_webapp

%postun
%_postun_webapp

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root, 0755)
%doc README
%lang(jp) %doc README.euc_jp
%dir %{_pgpoolAdmindir}
%config(noreplace) %{_webappconfdir}/%{short_name}.conf
%{_pgpoolAdmindir}/*.php
%dir %{_pgpoolAdmindir}/conf
%attr(644,apache,apache) %config(noreplace) %{_pgpoolAdmindir}/conf/*
%{_pgpoolAdmindir}/doc
%{_pgpoolAdmindir}/images
%{_pgpoolAdmindir}/install
%{_pgpoolAdmindir}/lang
%{_pgpoolAdmindir}/libs
%{_pgpoolAdmindir}/templates
%attr(755,apache,apache) %{_pgpoolAdmindir}/templates_c
%{_pgpoolAdmindir}/screen.css

