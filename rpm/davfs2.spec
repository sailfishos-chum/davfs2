# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.32
# 

Name:       davfs2

# >> macros
# << macros
%define dav_group mount
%define dav_user mount
%define dav_cachedir /home/.system/var/cache/%{name}

Summary:    Linux FUSE driver that allows you to mount a WebDAV resource
Version:    1.6.1
Release:    0
Group:      System
License:    GPLv3+
URL:        https://savannah.nongnu.org/projects/davfs2/
Source0:    https://download.savannah.nongnu.org/releases/davfs2/%{name}-%{version}.tar.gz
Source1:    davfs2-rpmlintrc
Source100:  davfs2.yaml
Patch0:     filelocations.patch
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(libproxy-1.0)
BuildRequires:  pkgconfig(libssl)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(neon)
BuildRequires:  pkgconfig(zlib)

%description
davfs2 is a Linux file system driver that allows you to mount a WebDAV
resource into your Unix file system tree. So - and that is what makes
davfs2 different - applications can use it without knowing about WebDAV.
You may edit WebDAV resources using standard applications that interact
with the file system as usual.

davfs2 supports SSL and proxy, HTTP authentication (basic and digest)
and client certificates.
%if "%{?vendor}" == "chum"
PackageName: davfs2
PackagerName: nephros
Type: console-application
Categories:
  - Network
  - System
  - Filesystem
%endif


%package doc
Summary:    Documentation for %{name}
Group:      Documentation
BuildArch:  noarch

%description doc
%{summary}.

%prep
%setup -q -n %{name}-%{version}

# filelocations.patch
%patch0 -p1
# >> setup
# << setup

%build
# >> build pre
# set the user/group in the system config file. note that this needs the patch above
sed -i "s#@@rpm_dav_user@@#%{dav_user}#"  etc/davfs2.conf
sed -i "s#@@rpm_dav_group@@#%{dav_group}#"  etc/davfs2.conf
sed -i "s#@@rpm_dav_cachedir@@#%{dav_cachedir}#"  etc/davfs2.conf
# << build pre

%configure --disable-static \
    --enable-largefile \
    --disable-nls \
    dav_group=%{dav_group} \
    dav_user=%{dav_user} \
    dav_syscachedir=%{dav_cachedir}

make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install

# >> install post
install -d -m 755 %{buildroot}%{dav_cachedir}
# << install post

%files
%defattr(-,root,root,-)
/sbin/*
%{_sbindir}/*
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.conf
%config(noreplace) %{_sysconfdir}/%{name}/secrets
%{_sysconfdir}/%{name}/certs
%{_datadir}/%{name}
%{dav_cachedir}
# >> files
# << files

%files doc
%defattr(-,root,root,-)
%{_mandir}/*/*
%{_docdir}/%{name}
# >> files doc
# << files doc
