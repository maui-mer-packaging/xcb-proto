# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       xcb-proto

# >> macros
# << macros

Summary:    XCB protocol
Version:    1.10
Release:    1
Group:      Development/Libraries
License:    MIT
URL:        http://xcb.freedesktop.org/
Source0:    http://xcb.freedesktop.org/dist/%{name}-%{version}.tar.bz2
Source100:  xcb-proto.yaml
BuildRequires:  python-devel

%description
Description: %{summary}

%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%configure --disable-static \
    --libdir=%{_datadir}

make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install

# >> install post

# << install post

%files
%defattr(-,root,root,-)
# >> files
%doc COPYING NEWS README TODO doc/xml-xcb.txt
%{_datadir}/pkgconfig/xcb-proto.pc
%dir %{_datadir}/xcb/
%{_datadir}/xcb/*.xsd
%{_datadir}/xcb/*.xml
%dir %{python_sitearch}/xcbgen/
%{python_sitearch}/xcbgen/*.py*
# << files
