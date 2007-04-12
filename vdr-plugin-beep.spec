
%define plugin	beep
%define name	vdr-plugin-%plugin
%define version	0.0.6
%define rel	9

Summary:	VDR plugin: Notify with a beep
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://deltab.de/vdr/beep.html
Source:		http://deltab.de/vdr/vdr-%plugin-%version.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.4.1-6
Requires:	vdr-abi = %vdr_abi

%description
This Plugin notify with a beep over the internal mainboard speaker,
to selected VDR events.

%prep
%setup -q -n %plugin-%version
chmod a+x contrib
chmod a+x contrib/Elise.sh

%build
%vdr_plugin_build

%install
rm -rf %{buildroot}
%vdr_plugin_install

%clean
rm -rf %{buildroot}

%post
%vdr_plugin_post %plugin

%postun
%vdr_plugin_postun %plugin

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY contrib


