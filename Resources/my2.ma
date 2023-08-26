//Maya ASCII 2018 scene
//Name: my2.ma
//Last modified: Tue, Aug 22, 2023 08:36:17 PM
//Codeset: 936
requires maya "2018";
requires "stereoCamera" "10.0";
currentUnit -l centimeter -a degree -t film;
fileInfo "application" "maya";
fileInfo "product" "Maya 2018";
fileInfo "version" "2018";
fileInfo "cutIdentifier" "201706261615-f9658c4cfc";
fileInfo "osv" "Microsoft Windows 8 Business Edition, 64-bit  (Build 9200)\n";
createNode transform -s -n "persp";
	rename -uid "6763456A-46D0-31B2-7F41-28B963C929DE";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 11.031765985270836 16.455914781414993 15.766018457870167 ;
	setAttr ".r" -type "double3" -14.738352729940241 394.19999999933049 1.9227598739263987e-15 ;
createNode camera -s -n "perspShape" -p "persp";
	rename -uid "25FF0A99-478C-B96B-7831-949F6E2EB352";
	setAttr -k off ".v" no;
	setAttr ".fl" 34.999999999999993;
	setAttr ".coi" 20.368402979438695;
	setAttr ".imn" -type "string" "persp";
	setAttr ".den" -type "string" "persp_depth";
	setAttr ".man" -type "string" "persp_mask";
	setAttr ".hc" -type "string" "viewSet -p %camera";
createNode transform -s -n "top";
	rename -uid "E5E015B6-40DB-71F8-93AD-51A8D0AAD9A3";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 1000.1 0 ;
	setAttr ".r" -type "double3" -89.999999999999986 0 0 ;
createNode camera -s -n "topShape" -p "top";
	rename -uid "FD192AC2-44C2-A7D4-6196-1DA0951DC032";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "top";
	setAttr ".den" -type "string" "top_depth";
	setAttr ".man" -type "string" "top_mask";
	setAttr ".hc" -type "string" "viewSet -t %camera";
	setAttr ".o" yes;
createNode transform -s -n "front";
	rename -uid "3E8D223A-4E0C-6378-0B75-E098F2DE2F14";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 5.8764406906826849 12.989896933543955 1000.1 ;
createNode camera -s -n "frontShape" -p "front";
	rename -uid "5AA72D5A-4D50-0984-8180-6BBC8488B309";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.1;
	setAttr ".ow" 26.15447942109839;
	setAttr ".imn" -type "string" "front";
	setAttr ".den" -type "string" "front_depth";
	setAttr ".man" -type "string" "front_mask";
	setAttr ".hc" -type "string" "viewSet -f %camera";
	setAttr ".o" yes;
createNode transform -s -n "side";
	rename -uid "6A54D32C-487E-A833-547B-8EBB9C89974A";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 1000.1 0.10571316945810116 0.79929118785097875 ;
	setAttr ".r" -type "double3" 0 89.999999999999986 0 ;
createNode camera -s -n "sideShape" -p "side";
	rename -uid "FAE2FD25-41BF-55B2-E0D5-4CA5C1A6E811";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.1;
	setAttr ".ow" 5.0087718783134596;
	setAttr ".imn" -type "string" "side";
	setAttr ".den" -type "string" "side_depth";
	setAttr ".man" -type "string" "side_mask";
	setAttr ".hc" -type "string" "viewSet -s %camera";
	setAttr ".o" yes;
createNode transform -n "Block";
	rename -uid "F1C5B344-4B97-4BF2-CA21-91853F599CA8";
	addAttr -ci true -sn "rigScale" -ln "rigScale" -dv 1 -min 0 -at "double";
	addAttr -ci true -sn "mainCount" -ln "mainCount" -dv 1 -min 1 -at "double";
	setAttr -l on ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr -k on ".rigScale";
	setAttr -k on ".mainCount";
createNode nurbsCurve -n "BlockShape" -p "Block";
	rename -uid "EDB68575-452E-606C-2E79-728E5887871F";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0 0.80779999 0.78819984 ;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		2.3508348746736734 1.439471202296542e-16 -2.3508348746736738
		2.0357196969332738e-16 2.0357196969332738e-16 -3.3245825626631631
		-2.3508348746736734 1.4394712022965415e-16 -2.3508348746736729
		-3.3245825626631644 1.0553206857018082e-32 -1.723469471257449e-16
		-2.3508348746736734 -1.4394712022965418e-16 2.3508348746736734
		-3.3302570908809675e-16 -2.0357196969332753e-16 3.3245825626631653
		2.3508348746736734 -1.4394712022965415e-16 2.3508348746736729
		3.3245825626631644 -2.7761037630330295e-32 4.533721502339877e-16
		2.3508348746736734 1.439471202296542e-16 -2.3508348746736738
		2.0357196969332738e-16 2.0357196969332738e-16 -3.3245825626631631
		-2.3508348746736734 1.4394712022965415e-16 -2.3508348746736729
		;
createNode joint -n "Root" -p "Block";
	rename -uid "6A2E6AE1-478D-57AB-EB87-D38D113DA5AC";
	addAttr -ci true -sn "n" -ln "name" -dt "string";
	addAttr -ci true -sn "mirror" -ln "mirror" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "ox" -ln "orientX" -min 0 -max 3 -en "Common:Parent:Free:World" 
		-at "enum";
	addAttr -ci true -sn "wx" -ln "worldX" -at "double3" -nc 3;
	addAttr -ci true -sn "wxx" -ln "worldXX" -at "double" -p "worldX";
	addAttr -ci true -sn "wxy" -ln "worldXY" -at "double" -p "worldX";
	addAttr -ci true -sn "wxz" -ln "worldXZ" -at "double" -p "worldX";
	addAttr -ci true -sn "oy" -ln "orientY" -min 0 -max 3 -en "Common:Parent:Free:World" 
		-at "enum";
	addAttr -ci true -sn "wy" -ln "worldY" -at "double3" -nc 3;
	addAttr -ci true -sn "wyx" -ln "worldYX" -at "double" -p "worldY";
	addAttr -ci true -sn "wyy" -ln "worldYY" -at "double" -p "worldY";
	addAttr -ci true -sn "wyz" -ln "worldYZ" -at "double" -p "worldY";
	addAttr -ci true -sn "secControl" -ln "secondControl" -dv 1 -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "subdivide" -ln "subdivide" -dv 2 -at "long";
	addAttr -ci true -sn "splineShape" -ln "splineShape" -min 0 -max 2 -en "FK:IK:Spline" 
		-at "enum";
	addAttr -ci true -sn "secShape" -ln "secShape" -min 0 -max 2 -en "FKSec:IKSec:SplineSec" 
		-at "enum";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.99215686 0.79607844 0.43137255 ;
	setAttr ".t" -type "double3" 1.9709482594718226e-16 9.8285102844238281 0 ;
	setAttr ".jo" -type "double3" -89.999999999999986 0 89.999999999999986 ;
	setAttr ".ssc" no;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "Spline";
	setAttr ".n" -type "string" "Default";
	setAttr ".wx" -type "double3" 1 0 0 ;
	setAttr ".wy" -type "double3" 0 1 0 ;
createNode joint -n "Spine" -p "Root";
	rename -uid "7EA14B72-46D4-F729-B979-8E8AE5406450";
	addAttr -ci true -sn "n" -ln "name" -dt "string";
	addAttr -ci true -sn "mirror" -ln "mirror" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "ox" -ln "orientX" -min 0 -max 3 -en "Common:Parent:Free:World" 
		-at "enum";
	addAttr -ci true -sn "wx" -ln "worldX" -at "double3" -nc 3;
	addAttr -ci true -sn "wxx" -ln "worldXX" -at "double" -p "worldX";
	addAttr -ci true -sn "wxy" -ln "worldXY" -at "double" -p "worldX";
	addAttr -ci true -sn "wxz" -ln "worldXZ" -at "double" -p "worldX";
	addAttr -ci true -sn "oy" -ln "orientY" -min 0 -max 3 -en "Common:Parent:Free:World" 
		-at "enum";
	addAttr -ci true -sn "wy" -ln "worldY" -at "double3" -nc 3;
	addAttr -ci true -sn "wyx" -ln "worldYX" -at "double" -p "worldY";
	addAttr -ci true -sn "wyy" -ln "worldYY" -at "double" -p "worldY";
	addAttr -ci true -sn "wyz" -ln "worldYZ" -at "double" -p "worldY";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.99215686 0.79607844 0.43137255 ;
	setAttr ".t" -type "double3" 1.7560000419616699 9.7477583891429349e-17 -3.899103355657174e-16 ;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "Child";
	setAttr ".n" -type "string" "Default";
	setAttr ".wx" -type "double3" 1 0 0 ;
	setAttr ".wy" -type "double3" 0 1 0 ;
createNode joint -n "Chest" -p "Spine";
	rename -uid "743BB571-49E3-34AD-BC40-E5B847AF8071";
	addAttr -ci true -sn "n" -ln "name" -dt "string";
	addAttr -ci true -sn "mirror" -ln "mirror" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "ox" -ln "orientX" -min 0 -max 3 -en "Common:Parent:Free:World" 
		-at "enum";
	addAttr -ci true -sn "wx" -ln "worldX" -at "double3" -nc 3;
	addAttr -ci true -sn "wxx" -ln "worldXX" -at "double" -p "worldX";
	addAttr -ci true -sn "wxy" -ln "worldXY" -at "double" -p "worldX";
	addAttr -ci true -sn "wxz" -ln "worldXZ" -at "double" -p "worldX";
	addAttr -ci true -sn "oy" -ln "orientY" -min 0 -max 3 -en "Common:Parent:Free:World" 
		-at "enum";
	addAttr -ci true -sn "wy" -ln "worldY" -at "double3" -nc 3;
	addAttr -ci true -sn "wyx" -ln "worldYX" -at "double" -p "worldY";
	addAttr -ci true -sn "wyy" -ln "worldYY" -at "double" -p "worldY";
	addAttr -ci true -sn "wyz" -ln "worldYZ" -at "double" -p "worldY";
	addAttr -ci true -sn "secControl" -ln "secondControl" -dv 1 -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "subdivide" -ln "subdivide" -dv 2 -at "long";
	addAttr -ci true -sn "fkShape" -ln "fkShape" -min 0 -max 1 -en "FK:IK" -at "enum";
	addAttr -ci true -sn "secShape" -ln "secShape" -min 0 -max 1 -en "FK:IK" -at "enum";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.45490196 0.72549021 1 ;
	setAttr ".t" -type "double3" 1.4259999990463257 -7.125485290171829e-32 -3.9443045261050599e-31 ;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "FK";
	setAttr ".n" -type "string" "Default";
	setAttr ".wx" -type "double3" 1 0 0 ;
	setAttr ".wy" -type "double3" 0 1 0 ;
createNode joint -n "Neck" -p "Chest";
	rename -uid "21AFE1EF-496D-3FCF-7876-FE8EA1411A18";
	addAttr -ci true -sn "n" -ln "name" -dt "string";
	addAttr -ci true -sn "mirror" -ln "mirror" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "ox" -ln "orientX" -min 0 -max 3 -en "Common:Parent:Free:World" 
		-at "enum";
	addAttr -ci true -sn "wx" -ln "worldX" -at "double3" -nc 3;
	addAttr -ci true -sn "wxx" -ln "worldXX" -at "double" -p "worldX";
	addAttr -ci true -sn "wxy" -ln "worldXY" -at "double" -p "worldX";
	addAttr -ci true -sn "wxz" -ln "worldXZ" -at "double" -p "worldX";
	addAttr -ci true -sn "oy" -ln "orientY" -min 0 -max 3 -en "Common:Parent:Free:World" 
		-at "enum";
	addAttr -ci true -sn "wy" -ln "worldY" -at "double3" -nc 3;
	addAttr -ci true -sn "wyx" -ln "worldYX" -at "double" -p "worldY";
	addAttr -ci true -sn "wyy" -ln "worldYY" -at "double" -p "worldY";
	addAttr -ci true -sn "wyz" -ln "worldYZ" -at "double" -p "worldY";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.45490196 0.72549021 1 ;
	setAttr ".t" -type "double3" 1.4493891000747681 -1.8203073871823611e-17 5.1696068514710155e-17 ;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "Child";
	setAttr ".n" -type "string" "Default";
	setAttr ".wx" -type "double3" 1 0 0 ;
	setAttr ".wy" -type "double3" 0 1 0 ;
createNode joint -n "Head" -p "Neck";
	rename -uid "604979B2-44C1-2C1C-34FB-C5BE5A78BD67";
	addAttr -ci true -sn "n" -ln "name" -dt "string";
	addAttr -ci true -sn "mirror" -ln "mirror" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "ox" -ln "orientX" -min 0 -max 3 -en "Common:Parent:Free:World" 
		-at "enum";
	addAttr -ci true -sn "wx" -ln "worldX" -at "double3" -nc 3;
	addAttr -ci true -sn "wxx" -ln "worldXX" -at "double" -p "worldX";
	addAttr -ci true -sn "wxy" -ln "worldXY" -at "double" -p "worldX";
	addAttr -ci true -sn "wxz" -ln "worldXZ" -at "double" -p "worldX";
	addAttr -ci true -sn "oy" -ln "orientY" -min 0 -max 3 -en "Common:Parent:Free:World" 
		-at "enum";
	addAttr -ci true -sn "wy" -ln "worldY" -at "double3" -nc 3;
	addAttr -ci true -sn "wyx" -ln "worldYX" -at "double" -p "worldY";
	addAttr -ci true -sn "wyy" -ln "worldYY" -at "double" -p "worldY";
	addAttr -ci true -sn "wyz" -ln "worldYZ" -at "double" -p "worldY";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.45490196 0.72549021 1 ;
	setAttr ".t" -type "double3" 1.2020894289016724 -9.5525009166246901e-18 2.4267718931962319e-16 ;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "Child";
	setAttr ".n" -type "string" "Default";
	setAttr ".wx" -type "double3" 1 0 0 ;
	setAttr ".wy" -type "double3" 0 1 0 ;
createNode joint -n "HeadEnd" -p "Head";
	rename -uid "E964468B-48CC-BEAD-EB53-F8ADBFB4C980";
	addAttr -ci true -sn "n" -ln "name" -dt "string";
	addAttr -ci true -sn "mirror" -ln "mirror" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "ox" -ln "orientX" -min 0 -max 3 -en "Common:Parent:Free:World" 
		-at "enum";
	addAttr -ci true -sn "wx" -ln "worldX" -at "double3" -nc 3;
	addAttr -ci true -sn "wxx" -ln "worldXX" -at "double" -p "worldX";
	addAttr -ci true -sn "wxy" -ln "worldXY" -at "double" -p "worldX";
	addAttr -ci true -sn "wxz" -ln "worldXZ" -at "double" -p "worldX";
	addAttr -ci true -sn "oy" -ln "orientY" -min 0 -max 3 -en "Common:Parent:Free:World" 
		-at "enum";
	addAttr -ci true -sn "wy" -ln "worldY" -at "double3" -nc 3;
	addAttr -ci true -sn "wyx" -ln "worldYX" -at "double" -p "worldY";
	addAttr -ci true -sn "wyy" -ln "worldYY" -at "double" -p "worldY";
	addAttr -ci true -sn "wyz" -ln "worldYZ" -at "double" -p "worldY";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 1 1 1 ;
	setAttr ".t" -type "double3" 1.5170962810516357 -5.5511151231257827e-17 1.6843152217967236e-16 ;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "End";
	setAttr ".n" -type "string" "Default";
	setAttr ".wx" -type "double3" 1 0 0 ;
	setAttr ".wy" -type "double3" 0 1 0 ;
createNode joint -n "Eye" -p "Head";
	rename -uid "50EF63CA-4651-4A09-C0EC-AB8D4AB094D8";
	addAttr -ci true -sn "n" -ln "name" -dt "string";
	addAttr -ci true -sn "mirror" -ln "mirror" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "ox" -ln "orientX" -min 0 -max 3 -en "Common:Parent:Free:World" 
		-at "enum";
	addAttr -ci true -sn "wx" -ln "worldX" -at "double3" -nc 3;
	addAttr -ci true -sn "wxx" -ln "worldXX" -at "double" -p "worldX";
	addAttr -ci true -sn "wxy" -ln "worldXY" -at "double" -p "worldX";
	addAttr -ci true -sn "wxz" -ln "worldXZ" -at "double" -p "worldX";
	addAttr -ci true -sn "oy" -ln "orientY" -min 0 -max 3 -en "Common:Parent:Free:World" 
		-at "enum";
	addAttr -ci true -sn "wy" -ln "worldY" -at "double3" -nc 3;
	addAttr -ci true -sn "wyx" -ln "worldYX" -at "double" -p "worldY";
	addAttr -ci true -sn "wyy" -ln "worldYY" -at "double" -p "worldY";
	addAttr -ci true -sn "wyz" -ln "worldYZ" -at "double" -p "worldY";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.45490196 0.72549021 1 ;
	setAttr ".t" -type "double3" 0.23521468043327332 -1.1152639389038086 -0.40199345350265503 ;
	setAttr ".jo" -type "double3" 0 0 -90.000000000001592 ;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "Child";
	setAttr ".n" -type "string" "Default";
	setAttr ".wx" -type "double3" 1 0 0 ;
	setAttr ".wy" -type "double3" 0 1 0 ;
createNode joint -n "EyeEnd" -p "Eye";
	rename -uid "19E0E9B7-4E27-2129-7747-55BFE137BA9C";
	addAttr -ci true -sn "n" -ln "name" -dt "string";
	addAttr -ci true -sn "mirror" -ln "mirror" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "ox" -ln "orientX" -min 0 -max 3 -en "Common:Parent:Free:World" 
		-at "enum";
	addAttr -ci true -sn "wx" -ln "worldX" -at "double3" -nc 3;
	addAttr -ci true -sn "wxx" -ln "worldXX" -at "double" -p "worldX";
	addAttr -ci true -sn "wxy" -ln "worldXY" -at "double" -p "worldX";
	addAttr -ci true -sn "wxz" -ln "worldXZ" -at "double" -p "worldX";
	addAttr -ci true -sn "oy" -ln "orientY" -min 0 -max 3 -en "Common:Parent:Free:World" 
		-at "enum";
	addAttr -ci true -sn "wy" -ln "worldY" -at "double3" -nc 3;
	addAttr -ci true -sn "wyx" -ln "worldYX" -at "double" -p "worldY";
	addAttr -ci true -sn "wyy" -ln "worldYY" -at "double" -p "worldY";
	addAttr -ci true -sn "wyz" -ln "worldYZ" -at "double" -p "worldY";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 1 1 1 ;
	setAttr ".t" -type "double3" 0.19217437505722046 1.5507742241766522e-17 -5.9855245728035212e-17 ;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "End";
	setAttr ".n" -type "string" "Default";
	setAttr ".wx" -type "double3" 1 0 0 ;
	setAttr ".wy" -type "double3" 0 1 0 ;
createNode joint -n "Jaw" -p "Head";
	rename -uid "70D24F83-4AB4-1715-C2AD-A6B386BE3314";
	addAttr -ci true -sn "n" -ln "name" -dt "string";
	addAttr -ci true -sn "mirror" -ln "mirror" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "ox" -ln "orientX" -min 0 -max 3 -en "Common:Parent:Free:World" 
		-at "enum";
	addAttr -ci true -sn "wx" -ln "worldX" -at "double3" -nc 3;
	addAttr -ci true -sn "wxx" -ln "worldXX" -at "double" -p "worldX";
	addAttr -ci true -sn "wxy" -ln "worldXY" -at "double" -p "worldX";
	addAttr -ci true -sn "wxz" -ln "worldXZ" -at "double" -p "worldX";
	addAttr -ci true -sn "oy" -ln "orientY" -min 0 -max 3 -en "Common:Parent:Free:World" 
		-at "enum";
	addAttr -ci true -sn "wy" -ln "worldY" -at "double3" -nc 3;
	addAttr -ci true -sn "wyx" -ln "worldYX" -at "double" -p "worldY";
	addAttr -ci true -sn "wyy" -ln "worldYY" -at "double" -p "worldY";
	addAttr -ci true -sn "wyz" -ln "worldYZ" -at "double" -p "worldY";
	setAttr ".v" no;
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.45490196 0.72549021 1 ;
	setAttr ".t" -type "double3" -0.28607422113418579 -0.41421523690223694 -1.3813750793513052e-17 ;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "Child";
	setAttr ".n" -type "string" "Default";
	setAttr ".wx" -type "double3" 1 0 0 ;
	setAttr ".wy" -type "double3" 0 1 0 ;
createNode joint -n "JawEnd" -p "Jaw";
	rename -uid "84BFA510-4137-1AE6-A347-C8A8439D4812";
	addAttr -ci true -sn "n" -ln "name" -dt "string";
	addAttr -ci true -sn "mirror" -ln "mirror" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "ox" -ln "orientX" -min 0 -max 3 -en "Common:Parent:Free:World" 
		-at "enum";
	addAttr -ci true -sn "wx" -ln "worldX" -at "double3" -nc 3;
	addAttr -ci true -sn "wxx" -ln "worldXX" -at "double" -p "worldX";
	addAttr -ci true -sn "wxy" -ln "worldXY" -at "double" -p "worldX";
	addAttr -ci true -sn "wxz" -ln "worldXZ" -at "double" -p "worldX";
	addAttr -ci true -sn "oy" -ln "orientY" -min 0 -max 3 -en "Common:Parent:Free:World" 
		-at "enum";
	addAttr -ci true -sn "wy" -ln "worldY" -at "double3" -nc 3;
	addAttr -ci true -sn "wyx" -ln "worldYX" -at "double" -p "worldY";
	addAttr -ci true -sn "wyy" -ln "worldYY" -at "double" -p "worldY";
	addAttr -ci true -sn "wyz" -ln "worldYZ" -at "double" -p "worldY";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 1 1 1 ;
	setAttr ".t" -type "double3" -0.46426934003829956 -0.99937278032302856 -1.7571812310842748e-16 ;
	setAttr ".jo" -type "double3" -5.6498000615042044e-30 0 0 ;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "End";
	setAttr ".n" -type "string" "Default";
	setAttr ".wx" -type "double3" 1 0 0 ;
	setAttr ".wy" -type "double3" 0 1 0 ;
createNode joint -n "Scapula" -p "Chest";
	rename -uid "1CEF013D-4C80-07ED-59FB-4C9A0ADA84E8";
	addAttr -ci true -sn "n" -ln "name" -dt "string";
	addAttr -ci true -sn "mirror" -ln "mirror" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "ox" -ln "orientX" -min 0 -max 3 -en "Common:Parent:Free:World" 
		-at "enum";
	addAttr -ci true -sn "wx" -ln "worldX" -at "double3" -nc 3;
	addAttr -ci true -sn "wxx" -ln "worldXX" -at "double" -p "worldX";
	addAttr -ci true -sn "wxy" -ln "worldXY" -at "double" -p "worldX";
	addAttr -ci true -sn "wxz" -ln "worldXZ" -at "double" -p "worldX";
	addAttr -ci true -sn "oy" -ln "orientY" -min 0 -max 3 -en "Common:Parent:Free:World" 
		-at "enum";
	addAttr -ci true -sn "wy" -ln "worldY" -at "double3" -nc 3;
	addAttr -ci true -sn "wyx" -ln "worldYX" -at "double" -p "worldY";
	addAttr -ci true -sn "wyy" -ln "worldYY" -at "double" -p "worldY";
	addAttr -ci true -sn "wyz" -ln "worldYZ" -at "double" -p "worldY";
	addAttr -ci true -sn "secControl" -ln "secondControl" -dv 1 -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "subdivide" -ln "subdivide" -dv 2 -at "long";
	addAttr -ci true -sn "fkShape" -ln "fkShape" -min 0 -max 1 -en "FK:IK" -at "enum";
	addAttr -ci true -sn "secShape" -ln "secShape" -min 0 -max 1 -en "FK:IK" -at "enum";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.45490196 0.72549021 1 ;
	setAttr ".t" -type "double3" 0.68687349557876587 -2.7755575615628914e-16 -0.48817041516304016 ;
	setAttr ".jo" -type "double3" -1.5902773407317587e-14 89.999999999999972 0 ;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "FK";
	setAttr ".n" -type "string" "Default";
	setAttr ".wx" -type "double3" 1 0 0 ;
	setAttr ".wy" -type "double3" 0 1 0 ;
createNode joint -n "Shoulder" -p "Scapula";
	rename -uid "3D7AED4B-496E-A834-238D-B3B232EC2FB4";
	addAttr -ci true -sn "n" -ln "name" -dt "string";
	addAttr -ci true -sn "mirror" -ln "mirror" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "ox" -ln "orientX" -min 0 -max 3 -en "Common:Parent:Free:World" 
		-at "enum";
	addAttr -ci true -sn "wx" -ln "worldX" -at "double3" -nc 3;
	addAttr -ci true -sn "wxx" -ln "worldXX" -at "double" -p "worldX";
	addAttr -ci true -sn "wxy" -ln "worldXY" -at "double" -p "worldX";
	addAttr -ci true -sn "wxz" -ln "worldXZ" -at "double" -p "worldX";
	addAttr -ci true -sn "oy" -ln "orientY" -min 0 -max 3 -en "Common:Parent:Free:World" 
		-at "enum";
	addAttr -ci true -sn "wy" -ln "worldY" -at "double3" -nc 3;
	addAttr -ci true -sn "wyx" -ln "worldYX" -at "double" -p "worldY";
	addAttr -ci true -sn "wyy" -ln "worldYY" -at "double" -p "worldY";
	addAttr -ci true -sn "wyz" -ln "worldYZ" -at "double" -p "worldY";
	addAttr -ci true -sn "secControl" -ln "secondControl" -dv 1 -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "subdivide" -ln "subdivide" -dv 2 -at "long";
	addAttr -ci true -sn "ikShape" -ln "ikShape" -min 0 -max 2 -en "FK:IK:Spline" -at "enum";
	addAttr -ci true -sn "secShape" -ln "secShape" -min 0 -max 2 -en "FKSec:IKSec:SplineSec" 
		-at "enum";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 1 0.4627451 0.45882353 ;
	setAttr ".t" -type "double3" 0.95341253280639648 5.9993517239229576e-16 -2.813987711077615e-16 ;
	setAttr ".jo" -type "double3" -2.8249000307521015e-30 0 0 ;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "IK";
	setAttr ".n" -type "string" "Default";
	setAttr ".wx" -type "double3" 1 0 0 ;
	setAttr ".wy" -type "double3" 0 1 0 ;
createNode joint -n "Elbow" -p "Shoulder";
	rename -uid "5CD9CAD5-4D17-4178-5DC5-209ECCDB72DE";
	addAttr -ci true -sn "n" -ln "name" -dt "string";
	addAttr -ci true -sn "mirror" -ln "mirror" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "ox" -ln "orientX" -min 0 -max 3 -en "Common:Parent:Free:World" 
		-at "enum";
	addAttr -ci true -sn "wx" -ln "worldX" -at "double3" -nc 3;
	addAttr -ci true -sn "wxx" -ln "worldXX" -at "double" -p "worldX";
	addAttr -ci true -sn "wxy" -ln "worldXY" -at "double" -p "worldX";
	addAttr -ci true -sn "wxz" -ln "worldXZ" -at "double" -p "worldX";
	addAttr -ci true -sn "oy" -ln "orientY" -min 0 -max 3 -en "Common:Parent:Free:World" 
		-at "enum";
	addAttr -ci true -sn "wy" -ln "worldY" -at "double3" -nc 3;
	addAttr -ci true -sn "wyx" -ln "worldYX" -at "double" -p "worldY";
	addAttr -ci true -sn "wyy" -ln "worldYY" -at "double" -p "worldY";
	addAttr -ci true -sn "wyz" -ln "worldYZ" -at "double" -p "worldY";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 1 0.4627451 0.45882353 ;
	setAttr ".t" -type "double3" 2.3484828472137451 2.4367472943369274e-16 3.6706270178054039e-15 ;
	setAttr ".jo" -type "double3" 0 -3.3479231403984686e-31 0 ;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "Child";
	setAttr ".n" -type "string" "Default";
	setAttr ".wx" -type "double3" 1 0 0 ;
	setAttr ".wy" -type "double3" 0 1 0 ;
createNode joint -n "Wrist" -p "Elbow";
	rename -uid "17339E7A-4E9F-6840-5F35-38AF61E6AF42";
	addAttr -ci true -sn "n" -ln "name" -dt "string";
	addAttr -ci true -sn "mirror" -ln "mirror" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "ox" -ln "orientX" -min 0 -max 3 -en "Common:Parent:Free:World" 
		-at "enum";
	addAttr -ci true -sn "wx" -ln "worldX" -at "double3" -nc 3;
	addAttr -ci true -sn "wxx" -ln "worldXX" -at "double" -p "worldX";
	addAttr -ci true -sn "wxy" -ln "worldXY" -at "double" -p "worldX";
	addAttr -ci true -sn "wxz" -ln "worldXZ" -at "double" -p "worldX";
	addAttr -ci true -sn "oy" -ln "orientY" -min 0 -max 3 -en "Common:Parent:Free:World" 
		-at "enum";
	addAttr -ci true -sn "wy" -ln "worldY" -at "double3" -nc 3;
	addAttr -ci true -sn "wyx" -ln "worldYX" -at "double" -p "worldY";
	addAttr -ci true -sn "wyy" -ln "worldYY" -at "double" -p "worldY";
	addAttr -ci true -sn "wyz" -ln "worldYZ" -at "double" -p "worldY";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 1 0.4627451 0.45882353 ;
	setAttr ".t" -type "double3" 2.1639010906219482 8.7257443168536571e-17 -5.2761800869082984e-15 ;
	setAttr ".jo" -type "double3" 0 -3.3479231403984686e-31 0 ;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "Hand";
	setAttr ".n" -type "string" "Default";
	setAttr ".wx" -type "double3" 1 0 0 ;
	setAttr ".wy" -type "double3" 0 1 0 ;
createNode joint -n "WristEnd" -p "Wrist";
	rename -uid "5AF0DBF5-49C6-DACE-E74B-8D97BF0798FE";
	addAttr -ci true -sn "n" -ln "name" -dt "string";
	addAttr -ci true -sn "mirror" -ln "mirror" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "ox" -ln "orientX" -min 0 -max 3 -en "Common:Parent:Free:World" 
		-at "enum";
	addAttr -ci true -sn "wx" -ln "worldX" -at "double3" -nc 3;
	addAttr -ci true -sn "wxx" -ln "worldXX" -at "double" -p "worldX";
	addAttr -ci true -sn "wxy" -ln "worldXY" -at "double" -p "worldX";
	addAttr -ci true -sn "wxz" -ln "worldXZ" -at "double" -p "worldX";
	addAttr -ci true -sn "oy" -ln "orientY" -min 0 -max 3 -en "Common:Parent:Free:World" 
		-at "enum";
	addAttr -ci true -sn "wy" -ln "worldY" -at "double3" -nc 3;
	addAttr -ci true -sn "wyx" -ln "worldYX" -at "double" -p "worldY";
	addAttr -ci true -sn "wyy" -ln "worldYY" -at "double" -p "worldY";
	addAttr -ci true -sn "wyz" -ln "worldYZ" -at "double" -p "worldY";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 1 1 1 ;
	setAttr ".t" -type "double3" 1.497046947479248 -9.6931401165172015e-16 -2.4411792354147579e-15 ;
	setAttr ".jo" -type "double3" 0 7.64465582498791e-45 5.6498000615042044e-30 ;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "End";
	setAttr ".n" -type "string" "Default";
	setAttr ".wx" -type "double3" 1 0 0 ;
	setAttr ".wy" -type "double3" 0 1 0 ;
createNode joint -n "PinkyFinger1" -p "Wrist";
	rename -uid "6D0A232D-4A22-1778-0E35-3787E1C7F9D5";
	addAttr -ci true -sn "n" -ln "name" -dt "string";
	addAttr -ci true -sn "mirror" -ln "mirror" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "ox" -ln "orientX" -min 0 -max 3 -en "Common:Parent:Free:World" 
		-at "enum";
	addAttr -ci true -sn "wx" -ln "worldX" -at "double3" -nc 3;
	addAttr -ci true -sn "wxx" -ln "worldXX" -at "double" -p "worldX";
	addAttr -ci true -sn "wxy" -ln "worldXY" -at "double" -p "worldX";
	addAttr -ci true -sn "wxz" -ln "worldXZ" -at "double" -p "worldX";
	addAttr -ci true -sn "oy" -ln "orientY" -min 0 -max 3 -en "Common:Parent:Free:World" 
		-at "enum";
	addAttr -ci true -sn "wy" -ln "worldY" -at "double3" -nc 3;
	addAttr -ci true -sn "wyx" -ln "worldYX" -at "double" -p "worldY";
	addAttr -ci true -sn "wyy" -ln "worldYY" -at "double" -p "worldY";
	addAttr -ci true -sn "wyz" -ln "worldYZ" -at "double" -p "worldY";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.45490196 0.72549021 1 ;
	setAttr ".t" -type "double3" 0.69284635782241821 0.31442996859550476 3.2275737292498333e-15 ;
	setAttr ".jo" -type "double3" 0 7.64465582498791e-45 5.6498000615042044e-30 ;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "Child";
	setAttr ".n" -type "string" "Default";
	setAttr ".wx" -type "double3" 1 0 0 ;
	setAttr ".wy" -type "double3" 0 1 0 ;
createNode joint -n "PinkyFinger2" -p "PinkyFinger1";
	rename -uid "67313050-4E78-8D2B-A1F1-1A8105315447";
	addAttr -ci true -sn "n" -ln "name" -dt "string";
	addAttr -ci true -sn "mirror" -ln "mirror" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "ox" -ln "orientX" -min 0 -max 3 -en "Common:Parent:Free:World" 
		-at "enum";
	addAttr -ci true -sn "wx" -ln "worldX" -at "double3" -nc 3;
	addAttr -ci true -sn "wxx" -ln "worldXX" -at "double" -p "worldX";
	addAttr -ci true -sn "wxy" -ln "worldXY" -at "double" -p "worldX";
	addAttr -ci true -sn "wxz" -ln "worldXZ" -at "double" -p "worldX";
	addAttr -ci true -sn "oy" -ln "orientY" -min 0 -max 3 -en "Common:Parent:Free:World" 
		-at "enum";
	addAttr -ci true -sn "wy" -ln "worldY" -at "double3" -nc 3;
	addAttr -ci true -sn "wyx" -ln "worldYX" -at "double" -p "worldY";
	addAttr -ci true -sn "wyy" -ln "worldYY" -at "double" -p "worldY";
	addAttr -ci true -sn "wyz" -ln "worldYZ" -at "double" -p "worldY";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.45490196 0.72549021 1 ;
	setAttr ".t" -type "double3" 0.25999999046325684 -7.058485691636675e-17 -1.8881150017356933e-15 ;
	setAttr ".jo" -type "double3" 0 7.64465582498791e-45 5.6498000615042044e-30 ;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "Child";
	setAttr ".n" -type "string" "Default";
	setAttr ".wx" -type "double3" 1 0 0 ;
	setAttr ".wy" -type "double3" 0 1 0 ;
createNode joint -n "PinkyFinger3" -p "PinkyFinger2";
	rename -uid "6781B82D-4871-5EEC-0827-1181DE497582";
	addAttr -ci true -sn "n" -ln "name" -dt "string";
	addAttr -ci true -sn "mirror" -ln "mirror" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "ox" -ln "orientX" -min 0 -max 3 -en "Common:Parent:Free:World" 
		-at "enum";
	addAttr -ci true -sn "wx" -ln "worldX" -at "double3" -nc 3;
	addAttr -ci true -sn "wxx" -ln "worldXX" -at "double" -p "worldX";
	addAttr -ci true -sn "wxy" -ln "worldXY" -at "double" -p "worldX";
	addAttr -ci true -sn "wxz" -ln "worldXZ" -at "double" -p "worldX";
	addAttr -ci true -sn "oy" -ln "orientY" -min 0 -max 3 -en "Common:Parent:Free:World" 
		-at "enum";
	addAttr -ci true -sn "wy" -ln "worldY" -at "double3" -nc 3;
	addAttr -ci true -sn "wyx" -ln "worldYX" -at "double" -p "worldY";
	addAttr -ci true -sn "wyy" -ln "worldYY" -at "double" -p "worldY";
	addAttr -ci true -sn "wyz" -ln "worldYZ" -at "double" -p "worldY";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.45490196 0.72549021 1 ;
	setAttr ".t" -type "double3" 0.15999999642372131 -7.0530861874701738e-18 -1.8490187137475134e-15 ;
	setAttr ".jo" -type "double3" 0 7.64465582498791e-45 5.6498000615042044e-30 ;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "Child";
	setAttr ".n" -type "string" "Default";
	setAttr ".wx" -type "double3" 1 0 0 ;
	setAttr ".wy" -type "double3" 0 1 0 ;
createNode joint -n "PinkyFingerEnd" -p "PinkyFinger3";
	rename -uid "F347815A-44C1-577C-50F5-45845E3BDD64";
	addAttr -ci true -sn "n" -ln "name" -dt "string";
	addAttr -ci true -sn "mirror" -ln "mirror" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "ox" -ln "orientX" -min 0 -max 3 -en "Common:Parent:Free:World" 
		-at "enum";
	addAttr -ci true -sn "wx" -ln "worldX" -at "double3" -nc 3;
	addAttr -ci true -sn "wxx" -ln "worldXX" -at "double" -p "worldX";
	addAttr -ci true -sn "wxy" -ln "worldXY" -at "double" -p "worldX";
	addAttr -ci true -sn "wxz" -ln "worldXZ" -at "double" -p "worldX";
	addAttr -ci true -sn "oy" -ln "orientY" -min 0 -max 3 -en "Common:Parent:Free:World" 
		-at "enum";
	addAttr -ci true -sn "wy" -ln "worldY" -at "double3" -nc 3;
	addAttr -ci true -sn "wyx" -ln "worldYX" -at "double" -p "worldY";
	addAttr -ci true -sn "wyy" -ln "worldYY" -at "double" -p "worldY";
	addAttr -ci true -sn "wyz" -ln "worldYZ" -at "double" -p "worldY";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 1 1 1 ;
	setAttr ".t" -type "double3" 0.15999999642372131 -3.3292060891568838e-17 -8.8808836950992026e-17 ;
	setAttr ".jo" -type "double3" 0 7.64465582498791e-45 5.6498000615042044e-30 ;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "End";
	setAttr ".n" -type "string" "Default";
	setAttr ".wx" -type "double3" 1 0 0 ;
	setAttr ".wy" -type "double3" 0 1 0 ;
createNode joint -n "RingFinger1" -p "Wrist";
	rename -uid "7DF5F6C3-4CA0-CCED-E928-C1A722777E4F";
	addAttr -ci true -sn "n" -ln "name" -dt "string";
	addAttr -ci true -sn "mirror" -ln "mirror" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "ox" -ln "orientX" -min 0 -max 3 -en "Common:Parent:Free:World" 
		-at "enum";
	addAttr -ci true -sn "wx" -ln "worldX" -at "double3" -nc 3;
	addAttr -ci true -sn "wxx" -ln "worldXX" -at "double" -p "worldX";
	addAttr -ci true -sn "wxy" -ln "worldXY" -at "double" -p "worldX";
	addAttr -ci true -sn "wxz" -ln "worldXZ" -at "double" -p "worldX";
	addAttr -ci true -sn "oy" -ln "orientY" -min 0 -max 3 -en "Common:Parent:Free:World" 
		-at "enum";
	addAttr -ci true -sn "wy" -ln "worldY" -at "double3" -nc 3;
	addAttr -ci true -sn "wyx" -ln "worldYX" -at "double" -p "worldY";
	addAttr -ci true -sn "wyy" -ln "worldYY" -at "double" -p "worldY";
	addAttr -ci true -sn "wyz" -ln "worldYZ" -at "double" -p "worldY";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.45490196 0.72549021 1 ;
	setAttr ".t" -type "double3" 0.69284635782241821 0.14338617026805878 3.2370685450720804e-15 ;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "Child";
	setAttr ".n" -type "string" "Default";
	setAttr ".wx" -type "double3" 1 0 0 ;
	setAttr ".wy" -type "double3" 0 1 0 ;
createNode joint -n "RingFinger2" -p "RingFinger1";
	rename -uid "96BD36E3-4A6B-A04B-CE68-72B037A304D9";
	addAttr -ci true -sn "n" -ln "name" -dt "string";
	addAttr -ci true -sn "mirror" -ln "mirror" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "ox" -ln "orientX" -min 0 -max 3 -en "Common:Parent:Free:World" 
		-at "enum";
	addAttr -ci true -sn "wx" -ln "worldX" -at "double3" -nc 3;
	addAttr -ci true -sn "wxx" -ln "worldXX" -at "double" -p "worldX";
	addAttr -ci true -sn "wxy" -ln "worldXY" -at "double" -p "worldX";
	addAttr -ci true -sn "wxz" -ln "worldXZ" -at "double" -p "worldX";
	addAttr -ci true -sn "oy" -ln "orientY" -min 0 -max 3 -en "Common:Parent:Free:World" 
		-at "enum";
	addAttr -ci true -sn "wy" -ln "worldY" -at "double3" -nc 3;
	addAttr -ci true -sn "wyx" -ln "worldYX" -at "double" -p "worldY";
	addAttr -ci true -sn "wyy" -ln "worldYY" -at "double" -p "worldY";
	addAttr -ci true -sn "wyz" -ln "worldYZ" -at "double" -p "worldY";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.45490196 0.72549021 1 ;
	setAttr ".t" -type "double3" 0.25999999046325684 -7.058485691636675e-17 -1.8881150017356933e-15 ;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "Child";
	setAttr ".n" -type "string" "Default";
	setAttr ".wx" -type "double3" 1 0 0 ;
	setAttr ".wy" -type "double3" 0 1 0 ;
createNode joint -n "RingFinger3" -p "RingFinger2";
	rename -uid "E105E189-44D2-05EC-22E7-FAA108CEF708";
	addAttr -ci true -sn "n" -ln "name" -dt "string";
	addAttr -ci true -sn "mirror" -ln "mirror" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "ox" -ln "orientX" -min 0 -max 3 -en "Common:Parent:Free:World" 
		-at "enum";
	addAttr -ci true -sn "wx" -ln "worldX" -at "double3" -nc 3;
	addAttr -ci true -sn "wxx" -ln "worldXX" -at "double" -p "worldX";
	addAttr -ci true -sn "wxy" -ln "worldXY" -at "double" -p "worldX";
	addAttr -ci true -sn "wxz" -ln "worldXZ" -at "double" -p "worldX";
	addAttr -ci true -sn "oy" -ln "orientY" -min 0 -max 3 -en "Common:Parent:Free:World" 
		-at "enum";
	addAttr -ci true -sn "wy" -ln "worldY" -at "double3" -nc 3;
	addAttr -ci true -sn "wyx" -ln "worldYX" -at "double" -p "worldY";
	addAttr -ci true -sn "wyy" -ln "worldYY" -at "double" -p "worldY";
	addAttr -ci true -sn "wyz" -ln "worldYZ" -at "double" -p "worldY";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.45490196 0.72549021 1 ;
	setAttr ".t" -type "double3" 0.15999999642372131 -7.0530861874701738e-18 -1.8490187137475134e-15 ;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "Child";
	setAttr ".n" -type "string" "Default";
	setAttr ".wx" -type "double3" 1 0 0 ;
	setAttr ".wy" -type "double3" 0 1 0 ;
createNode joint -n "RingFingerEnd" -p "RingFinger3";
	rename -uid "D5C33E5F-4724-B03F-18BD-DF940B0F0659";
	addAttr -ci true -sn "n" -ln "name" -dt "string";
	addAttr -ci true -sn "mirror" -ln "mirror" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "ox" -ln "orientX" -min 0 -max 3 -en "Common:Parent:Free:World" 
		-at "enum";
	addAttr -ci true -sn "wx" -ln "worldX" -at "double3" -nc 3;
	addAttr -ci true -sn "wxx" -ln "worldXX" -at "double" -p "worldX";
	addAttr -ci true -sn "wxy" -ln "worldXY" -at "double" -p "worldX";
	addAttr -ci true -sn "wxz" -ln "worldXZ" -at "double" -p "worldX";
	addAttr -ci true -sn "oy" -ln "orientY" -min 0 -max 3 -en "Common:Parent:Free:World" 
		-at "enum";
	addAttr -ci true -sn "wy" -ln "worldY" -at "double3" -nc 3;
	addAttr -ci true -sn "wyx" -ln "worldYX" -at "double" -p "worldY";
	addAttr -ci true -sn "wyy" -ln "worldYY" -at "double" -p "worldY";
	addAttr -ci true -sn "wyz" -ln "worldYZ" -at "double" -p "worldY";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 1 1 1 ;
	setAttr ".t" -type "double3" 0.15999999642372131 -3.3292060891568838e-17 -8.8808836950992026e-17 ;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "End";
	setAttr ".n" -type "string" "Default";
	setAttr ".wx" -type "double3" 1 0 0 ;
	setAttr ".wy" -type "double3" 0 1 0 ;
createNode joint -n "MiddleFinger1" -p "Wrist";
	rename -uid "DA6FF54A-4202-7AFC-7AB0-27B1922AC332";
	addAttr -ci true -sn "n" -ln "name" -dt "string";
	addAttr -ci true -sn "mirror" -ln "mirror" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "ox" -ln "orientX" -min 0 -max 3 -en "Common:Parent:Free:World" 
		-at "enum";
	addAttr -ci true -sn "wx" -ln "worldX" -at "double3" -nc 3;
	addAttr -ci true -sn "wxx" -ln "worldXX" -at "double" -p "worldX";
	addAttr -ci true -sn "wxy" -ln "worldXY" -at "double" -p "worldX";
	addAttr -ci true -sn "wxz" -ln "worldXZ" -at "double" -p "worldX";
	addAttr -ci true -sn "oy" -ln "orientY" -min 0 -max 3 -en "Common:Parent:Free:World" 
		-at "enum";
	addAttr -ci true -sn "wy" -ln "worldY" -at "double3" -nc 3;
	addAttr -ci true -sn "wyx" -ln "worldYX" -at "double" -p "worldY";
	addAttr -ci true -sn "wyy" -ln "worldYY" -at "double" -p "worldY";
	addAttr -ci true -sn "wyz" -ln "worldYZ" -at "double" -p "worldY";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.45490196 0.72549021 1 ;
	setAttr ".t" -type "double3" 0.69284635782241821 -0.030421288684010506 3.2457205631118095e-15 ;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "Child";
	setAttr ".n" -type "string" "Default";
	setAttr ".wx" -type "double3" 1 0 0 ;
	setAttr ".wy" -type "double3" 0 1 0 ;
createNode joint -n "MiddleFinge2" -p "MiddleFinger1";
	rename -uid "D495ECD3-4DAF-F34F-ECB3-DAB42A3085D4";
	addAttr -ci true -sn "n" -ln "name" -dt "string";
	addAttr -ci true -sn "mirror" -ln "mirror" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "ox" -ln "orientX" -min 0 -max 3 -en "Common:Parent:Free:World" 
		-at "enum";
	addAttr -ci true -sn "wx" -ln "worldX" -at "double3" -nc 3;
	addAttr -ci true -sn "wxx" -ln "worldXX" -at "double" -p "worldX";
	addAttr -ci true -sn "wxy" -ln "worldXY" -at "double" -p "worldX";
	addAttr -ci true -sn "wxz" -ln "worldXZ" -at "double" -p "worldX";
	addAttr -ci true -sn "oy" -ln "orientY" -min 0 -max 3 -en "Common:Parent:Free:World" 
		-at "enum";
	addAttr -ci true -sn "wy" -ln "worldY" -at "double3" -nc 3;
	addAttr -ci true -sn "wyx" -ln "worldYX" -at "double" -p "worldY";
	addAttr -ci true -sn "wyy" -ln "worldYY" -at "double" -p "worldY";
	addAttr -ci true -sn "wyz" -ln "worldYZ" -at "double" -p "worldY";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.45490196 0.72549021 1 ;
	setAttr ".t" -type "double3" 0.25999999046325684 -7.058485691636675e-17 -1.8881150017356933e-15 ;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "Child";
	setAttr ".n" -type "string" "Default";
	setAttr ".wx" -type "double3" 1 0 0 ;
	setAttr ".wy" -type "double3" 0 1 0 ;
createNode joint -n "MiddleFinger3" -p "MiddleFinge2";
	rename -uid "0FBB698B-4263-90A6-6A2D-3CAC9569194A";
	addAttr -ci true -sn "n" -ln "name" -dt "string";
	addAttr -ci true -sn "mirror" -ln "mirror" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "ox" -ln "orientX" -min 0 -max 3 -en "Common:Parent:Free:World" 
		-at "enum";
	addAttr -ci true -sn "wx" -ln "worldX" -at "double3" -nc 3;
	addAttr -ci true -sn "wxx" -ln "worldXX" -at "double" -p "worldX";
	addAttr -ci true -sn "wxy" -ln "worldXY" -at "double" -p "worldX";
	addAttr -ci true -sn "wxz" -ln "worldXZ" -at "double" -p "worldX";
	addAttr -ci true -sn "oy" -ln "orientY" -min 0 -max 3 -en "Common:Parent:Free:World" 
		-at "enum";
	addAttr -ci true -sn "wy" -ln "worldY" -at "double3" -nc 3;
	addAttr -ci true -sn "wyx" -ln "worldYX" -at "double" -p "worldY";
	addAttr -ci true -sn "wyy" -ln "worldYY" -at "double" -p "worldY";
	addAttr -ci true -sn "wyz" -ln "worldYZ" -at "double" -p "worldY";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.45490196 0.72549021 1 ;
	setAttr ".t" -type "double3" 0.15999999642372131 -7.0530861874701738e-18 -1.8490187137475134e-15 ;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "Child";
	setAttr ".n" -type "string" "Default";
	setAttr ".wx" -type "double3" 1 0 0 ;
	setAttr ".wy" -type "double3" 0 1 0 ;
createNode joint -n "MiddleFingerEnd" -p "MiddleFinger3";
	rename -uid "2C39BD55-4DFE-1693-D3B0-BC999028183B";
	addAttr -ci true -sn "n" -ln "name" -dt "string";
	addAttr -ci true -sn "mirror" -ln "mirror" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "ox" -ln "orientX" -min 0 -max 3 -en "Common:Parent:Free:World" 
		-at "enum";
	addAttr -ci true -sn "wx" -ln "worldX" -at "double3" -nc 3;
	addAttr -ci true -sn "wxx" -ln "worldXX" -at "double" -p "worldX";
	addAttr -ci true -sn "wxy" -ln "worldXY" -at "double" -p "worldX";
	addAttr -ci true -sn "wxz" -ln "worldXZ" -at "double" -p "worldX";
	addAttr -ci true -sn "oy" -ln "orientY" -min 0 -max 3 -en "Common:Parent:Free:World" 
		-at "enum";
	addAttr -ci true -sn "wy" -ln "worldY" -at "double3" -nc 3;
	addAttr -ci true -sn "wyx" -ln "worldYX" -at "double" -p "worldY";
	addAttr -ci true -sn "wyy" -ln "worldYY" -at "double" -p "worldY";
	addAttr -ci true -sn "wyz" -ln "worldYZ" -at "double" -p "worldY";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 1 1 1 ;
	setAttr ".t" -type "double3" 0.15999999642372131 -3.3292060891568838e-17 -8.8808836950992026e-17 ;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "End";
	setAttr ".n" -type "string" "Default";
	setAttr ".wx" -type "double3" 1 0 0 ;
	setAttr ".wy" -type "double3" 0 1 0 ;
createNode joint -n "IndexFinger1" -p "Wrist";
	rename -uid "96CBC291-45B5-F468-E9C7-FF8776DA1634";
	addAttr -ci true -sn "n" -ln "name" -dt "string";
	addAttr -ci true -sn "mirror" -ln "mirror" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "ox" -ln "orientX" -min 0 -max 3 -en "Common:Parent:Free:World" 
		-at "enum";
	addAttr -ci true -sn "wx" -ln "worldX" -at "double3" -nc 3;
	addAttr -ci true -sn "wxx" -ln "worldXX" -at "double" -p "worldX";
	addAttr -ci true -sn "wxy" -ln "worldXY" -at "double" -p "worldX";
	addAttr -ci true -sn "wxz" -ln "worldXZ" -at "double" -p "worldX";
	addAttr -ci true -sn "oy" -ln "orientY" -min 0 -max 3 -en "Common:Parent:Free:World" 
		-at "enum";
	addAttr -ci true -sn "wy" -ln "worldY" -at "double3" -nc 3;
	addAttr -ci true -sn "wyx" -ln "worldYX" -at "double" -p "worldY";
	addAttr -ci true -sn "wyy" -ln "worldYY" -at "double" -p "worldY";
	addAttr -ci true -sn "wyz" -ln "worldYZ" -at "double" -p "worldY";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.45490196 0.72549021 1 ;
	setAttr ".t" -type "double3" 0.69284635782241821 -0.21325623989105225 3.2558699236440473e-15 ;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "Child";
	setAttr ".n" -type "string" "Default";
	setAttr ".wx" -type "double3" 1 0 0 ;
	setAttr ".wy" -type "double3" 0 1 0 ;
createNode joint -n "IndexFinger2" -p "IndexFinger1";
	rename -uid "46726E00-41EE-A8EC-22FB-6C92450B5572";
	addAttr -ci true -sn "n" -ln "name" -dt "string";
	addAttr -ci true -sn "mirror" -ln "mirror" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "ox" -ln "orientX" -min 0 -max 3 -en "Common:Parent:Free:World" 
		-at "enum";
	addAttr -ci true -sn "wx" -ln "worldX" -at "double3" -nc 3;
	addAttr -ci true -sn "wxx" -ln "worldXX" -at "double" -p "worldX";
	addAttr -ci true -sn "wxy" -ln "worldXY" -at "double" -p "worldX";
	addAttr -ci true -sn "wxz" -ln "worldXZ" -at "double" -p "worldX";
	addAttr -ci true -sn "oy" -ln "orientY" -min 0 -max 3 -en "Common:Parent:Free:World" 
		-at "enum";
	addAttr -ci true -sn "wy" -ln "worldY" -at "double3" -nc 3;
	addAttr -ci true -sn "wyx" -ln "worldYX" -at "double" -p "worldY";
	addAttr -ci true -sn "wyy" -ln "worldYY" -at "double" -p "worldY";
	addAttr -ci true -sn "wyz" -ln "worldYZ" -at "double" -p "worldY";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.45490196 0.72549021 1 ;
	setAttr ".t" -type "double3" 0.25999999046325684 -7.058485691636675e-17 -1.8881150017356933e-15 ;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "Child";
	setAttr ".n" -type "string" "Default";
	setAttr ".wx" -type "double3" 1 0 0 ;
	setAttr ".wy" -type "double3" 0 1 0 ;
createNode joint -n "IndexFinger3" -p "IndexFinger2";
	rename -uid "27351D2C-416E-BB6F-A819-0891E4A15E90";
	addAttr -ci true -sn "n" -ln "name" -dt "string";
	addAttr -ci true -sn "mirror" -ln "mirror" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "ox" -ln "orientX" -min 0 -max 3 -en "Common:Parent:Free:World" 
		-at "enum";
	addAttr -ci true -sn "wx" -ln "worldX" -at "double3" -nc 3;
	addAttr -ci true -sn "wxx" -ln "worldXX" -at "double" -p "worldX";
	addAttr -ci true -sn "wxy" -ln "worldXY" -at "double" -p "worldX";
	addAttr -ci true -sn "wxz" -ln "worldXZ" -at "double" -p "worldX";
	addAttr -ci true -sn "oy" -ln "orientY" -min 0 -max 3 -en "Common:Parent:Free:World" 
		-at "enum";
	addAttr -ci true -sn "wy" -ln "worldY" -at "double3" -nc 3;
	addAttr -ci true -sn "wyx" -ln "worldYX" -at "double" -p "worldY";
	addAttr -ci true -sn "wyy" -ln "worldYY" -at "double" -p "worldY";
	addAttr -ci true -sn "wyz" -ln "worldYZ" -at "double" -p "worldY";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.45490196 0.72549021 1 ;
	setAttr ".t" -type "double3" 0.15999999642372131 -7.0530861874701738e-18 -1.8490187137475134e-15 ;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "Child";
	setAttr ".n" -type "string" "Default";
	setAttr ".wx" -type "double3" 1 0 0 ;
	setAttr ".wy" -type "double3" 0 1 0 ;
createNode joint -n "IndexFingerEnd" -p "IndexFinger3";
	rename -uid "A9ED632F-4F62-ACF5-D3F7-18BAADDCE915";
	addAttr -ci true -sn "n" -ln "name" -dt "string";
	addAttr -ci true -sn "mirror" -ln "mirror" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "ox" -ln "orientX" -min 0 -max 3 -en "Common:Parent:Free:World" 
		-at "enum";
	addAttr -ci true -sn "wx" -ln "worldX" -at "double3" -nc 3;
	addAttr -ci true -sn "wxx" -ln "worldXX" -at "double" -p "worldX";
	addAttr -ci true -sn "wxy" -ln "worldXY" -at "double" -p "worldX";
	addAttr -ci true -sn "wxz" -ln "worldXZ" -at "double" -p "worldX";
	addAttr -ci true -sn "oy" -ln "orientY" -min 0 -max 3 -en "Common:Parent:Free:World" 
		-at "enum";
	addAttr -ci true -sn "wy" -ln "worldY" -at "double3" -nc 3;
	addAttr -ci true -sn "wyx" -ln "worldYX" -at "double" -p "worldY";
	addAttr -ci true -sn "wyy" -ln "worldYY" -at "double" -p "worldY";
	addAttr -ci true -sn "wyz" -ln "worldYZ" -at "double" -p "worldY";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 1 1 1 ;
	setAttr ".t" -type "double3" 0.15999999642372131 -3.3292060891568838e-17 -8.8808836950992026e-17 ;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "End";
	setAttr ".n" -type "string" "Default";
	setAttr ".wx" -type "double3" 1 0 0 ;
	setAttr ".wy" -type "double3" 0 1 0 ;
createNode joint -n "ThumbFinger1" -p "Wrist";
	rename -uid "7CD2F437-4F79-D963-63EB-489F0AA1458D";
	addAttr -ci true -sn "n" -ln "name" -dt "string";
	addAttr -ci true -sn "mirror" -ln "mirror" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "ox" -ln "orientX" -min 0 -max 3 -en "Common:Parent:Free:World" 
		-at "enum";
	addAttr -ci true -sn "wx" -ln "worldX" -at "double3" -nc 3;
	addAttr -ci true -sn "wxx" -ln "worldXX" -at "double" -p "worldX";
	addAttr -ci true -sn "wxy" -ln "worldXY" -at "double" -p "worldX";
	addAttr -ci true -sn "wxz" -ln "worldXZ" -at "double" -p "worldX";
	addAttr -ci true -sn "oy" -ln "orientY" -min 0 -max 3 -en "Common:Parent:Free:World" 
		-at "enum";
	addAttr -ci true -sn "wy" -ln "worldY" -at "double3" -nc 3;
	addAttr -ci true -sn "wyx" -ln "worldYX" -at "double" -p "worldY";
	addAttr -ci true -sn "wyy" -ln "worldYY" -at "double" -p "worldY";
	addAttr -ci true -sn "wyz" -ln "worldYZ" -at "double" -p "worldY";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.45490196 0.72549021 1 ;
	setAttr ".t" -type "double3" 0.23020651936531067 -0.13806571066379547 -0.11935640126466751 ;
	setAttr ".jo" -type "double3" 132.21872708305219 23.971773899091612 -30.953105315718304 ;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "Child";
	setAttr ".n" -type "string" "Default";
	setAttr ".wx" -type "double3" 1 0 0 ;
	setAttr ".wy" -type "double3" 0 1 0 ;
createNode joint -n "ThumbFinger2" -p "ThumbFinger1";
	rename -uid "7EB48318-47D2-A854-AE0D-58828969B3C7";
	addAttr -ci true -sn "n" -ln "name" -dt "string";
	addAttr -ci true -sn "mirror" -ln "mirror" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "ox" -ln "orientX" -min 0 -max 3 -en "Common:Parent:Free:World" 
		-at "enum";
	addAttr -ci true -sn "wx" -ln "worldX" -at "double3" -nc 3;
	addAttr -ci true -sn "wxx" -ln "worldXX" -at "double" -p "worldX";
	addAttr -ci true -sn "wxy" -ln "worldXY" -at "double" -p "worldX";
	addAttr -ci true -sn "wxz" -ln "worldXZ" -at "double" -p "worldX";
	addAttr -ci true -sn "oy" -ln "orientY" -min 0 -max 3 -en "Common:Parent:Free:World" 
		-at "enum";
	addAttr -ci true -sn "wy" -ln "worldY" -at "double3" -nc 3;
	addAttr -ci true -sn "wyx" -ln "worldYX" -at "double" -p "worldY";
	addAttr -ci true -sn "wyy" -ln "worldYY" -at "double" -p "worldY";
	addAttr -ci true -sn "wyz" -ln "worldYZ" -at "double" -p "worldY";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.45490196 0.72549021 1 ;
	setAttr ".t" -type "double3" 0.25999999046325684 -3.5527136788005009e-15 -3.5527136788005009e-15 ;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "Child";
	setAttr ".n" -type "string" "Default";
	setAttr ".wx" -type "double3" 1 0 0 ;
	setAttr ".wy" -type "double3" 0 1 0 ;
createNode joint -n "ThumbFinger3" -p "ThumbFinger2";
	rename -uid "2D379A9E-445B-1BD3-2EE9-7AB20FCC6513";
	addAttr -ci true -sn "n" -ln "name" -dt "string";
	addAttr -ci true -sn "mirror" -ln "mirror" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "ox" -ln "orientX" -min 0 -max 3 -en "Common:Parent:Free:World" 
		-at "enum";
	addAttr -ci true -sn "wx" -ln "worldX" -at "double3" -nc 3;
	addAttr -ci true -sn "wxx" -ln "worldXX" -at "double" -p "worldX";
	addAttr -ci true -sn "wxy" -ln "worldXY" -at "double" -p "worldX";
	addAttr -ci true -sn "wxz" -ln "worldXZ" -at "double" -p "worldX";
	addAttr -ci true -sn "oy" -ln "orientY" -min 0 -max 3 -en "Common:Parent:Free:World" 
		-at "enum";
	addAttr -ci true -sn "wy" -ln "worldY" -at "double3" -nc 3;
	addAttr -ci true -sn "wyx" -ln "worldYX" -at "double" -p "worldY";
	addAttr -ci true -sn "wyy" -ln "worldYY" -at "double" -p "worldY";
	addAttr -ci true -sn "wyz" -ln "worldYZ" -at "double" -p "worldY";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.45490196 0.72549021 1 ;
	setAttr ".t" -type "double3" 0.15999999642372131 1.7763568394002505e-15 -3.5527136788005009e-15 ;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "Child";
	setAttr ".n" -type "string" "Default";
	setAttr ".wx" -type "double3" 1 0 0 ;
	setAttr ".wy" -type "double3" 0 1 0 ;
createNode joint -n "ThumbFingerEnd" -p "ThumbFinger3";
	rename -uid "EBCF309D-4A5C-A93B-CFD0-19BCD05A1AC2";
	addAttr -ci true -sn "n" -ln "name" -dt "string";
	addAttr -ci true -sn "mirror" -ln "mirror" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "ox" -ln "orientX" -min 0 -max 3 -en "Common:Parent:Free:World" 
		-at "enum";
	addAttr -ci true -sn "wx" -ln "worldX" -at "double3" -nc 3;
	addAttr -ci true -sn "wxx" -ln "worldXX" -at "double" -p "worldX";
	addAttr -ci true -sn "wxy" -ln "worldXY" -at "double" -p "worldX";
	addAttr -ci true -sn "wxz" -ln "worldXZ" -at "double" -p "worldX";
	addAttr -ci true -sn "oy" -ln "orientY" -min 0 -max 3 -en "Common:Parent:Free:World" 
		-at "enum";
	addAttr -ci true -sn "wy" -ln "worldY" -at "double3" -nc 3;
	addAttr -ci true -sn "wyx" -ln "worldYX" -at "double" -p "worldY";
	addAttr -ci true -sn "wyy" -ln "worldYY" -at "double" -p "worldY";
	addAttr -ci true -sn "wyz" -ln "worldYZ" -at "double" -p "worldY";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 1 1 1 ;
	setAttr ".t" -type "double3" 0.15999999642372131 0 1.7763568394002505e-15 ;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "End";
	setAttr ".n" -type "string" "Default";
	setAttr ".wx" -type "double3" 1 0 0 ;
	setAttr ".wy" -type "double3" 0 1 0 ;
createNode transform -n "Hand_Driven_Pivot" -p "Wrist";
	rename -uid "5F22555B-47CB-D9C1-D657-E08D47D08F47";
	setAttr ".t" -type "double3" 0.31443320501371197 0 0.35190002116111607 ;
	setAttr ".r" -type "double3" 90.000000000000014 0 0 ;
	setAttr ".s" -type "double3" 0.99999999999999978 0.99999999999999978 0.99999999999999978 ;
createNode locator -n "Hand_Driven_PivotShape" -p "Hand_Driven_Pivot";
	rename -uid "EEA61235-4D94-80F7-8E6F-D2AA5B9A6D7F";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 1 1 0 ;
	setAttr ".los" -type "double3" 0.1 0.1 0.1 ;
createNode transform -n "Arm_Switch_Pivot" -p "Shoulder";
	rename -uid "E5E97128-456E-70ED-D75A-50A41731F558";
	setAttr ".t" -type "double3" 1.1694837539124776 0 0.83482051236944699 ;
	setAttr ".r" -type "double3" 90.000000000000014 0 0 ;
	setAttr ".s" -type "double3" 0.99999999999999978 0.99999999999999978 0.99999999999999978 ;
createNode locator -n "Arm_Switch_PivotShape" -p "Arm_Switch_Pivot";
	rename -uid "AB0258C5-4D60-0104-8AB4-FFA8C437DE77";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 1 1 0 ;
	setAttr ".los" -type "double3" 0.1 0.1 0.1 ;
createNode joint -n "Hip" -p "Root";
	rename -uid "731E93FB-4D9C-BCE5-E004-B885185E31EF";
	addAttr -ci true -sn "n" -ln "name" -dt "string";
	addAttr -ci true -sn "mirror" -ln "mirror" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "ox" -ln "orientX" -min 0 -max 3 -en "Common:Parent:Free:World" 
		-at "enum";
	addAttr -ci true -sn "wx" -ln "worldX" -at "double3" -nc 3;
	addAttr -ci true -sn "wxx" -ln "worldXX" -at "double" -p "worldX";
	addAttr -ci true -sn "wxy" -ln "worldXY" -at "double" -p "worldX";
	addAttr -ci true -sn "wxz" -ln "worldXZ" -at "double" -p "worldX";
	addAttr -ci true -sn "oy" -ln "orientY" -min 0 -max 3 -en "Common:Parent:Free:World" 
		-at "enum";
	addAttr -ci true -sn "wy" -ln "worldY" -at "double3" -nc 3;
	addAttr -ci true -sn "wyx" -ln "worldYX" -at "double" -p "worldY";
	addAttr -ci true -sn "wyy" -ln "worldYY" -at "double" -p "worldY";
	addAttr -ci true -sn "wyz" -ln "worldYZ" -at "double" -p "worldY";
	addAttr -ci true -sn "secControl" -ln "secondControl" -dv 1 -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "subdivide" -ln "subdivide" -dv 2 -at "long";
	addAttr -ci true -sn "ikShape" -ln "ikShape" -min 0 -max 2 -en "FK:IK:Spline" -at "enum";
	addAttr -ci true -sn "secShape" -ln "secShape" -min 0 -max 2 -en "FKSec:IKSec:SplineSec" 
		-at "enum";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 1 0.4627451 0.45882353 ;
	setAttr ".t" -type "double3" -0.26858851313591003 4.2999868442358932e-16 -1.1393146514892578 ;
	setAttr ".jo" -type "double3" -7.0167092985348752e-15 1.9852715252820869e-14 -180 ;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "IK";
	setAttr ".n" -type "string" "Default";
	setAttr ".wx" -type "double3" 1 0 0 ;
	setAttr ".wy" -type "double3" 0 1 0 ;
createNode joint -n "Knee" -p "Hip";
	rename -uid "4BE0A2AC-46E8-0E27-B89C-61842AD50845";
	addAttr -ci true -sn "n" -ln "name" -dt "string";
	addAttr -ci true -sn "mirror" -ln "mirror" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "ox" -ln "orientX" -min 0 -max 3 -en "Common:Parent:Free:World" 
		-at "enum";
	addAttr -ci true -sn "wx" -ln "worldX" -at "double3" -nc 3;
	addAttr -ci true -sn "wxx" -ln "worldXX" -at "double" -p "worldX";
	addAttr -ci true -sn "wxy" -ln "worldXY" -at "double" -p "worldX";
	addAttr -ci true -sn "wxz" -ln "worldXZ" -at "double" -p "worldX";
	addAttr -ci true -sn "oy" -ln "orientY" -min 0 -max 3 -en "Common:Parent:Free:World" 
		-at "enum";
	addAttr -ci true -sn "wy" -ln "worldY" -at "double3" -nc 3;
	addAttr -ci true -sn "wyx" -ln "worldYX" -at "double" -p "worldY";
	addAttr -ci true -sn "wyy" -ln "worldYY" -at "double" -p "worldY";
	addAttr -ci true -sn "wyz" -ln "worldYZ" -at "double" -p "worldY";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 1 0.4627451 0.45882353 ;
	setAttr ".t" -type "double3" 4.7348313331604004 -3.4177001210190729e-16 -8.8217994412590709e-16 ;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "Child";
	setAttr ".n" -type "string" "Default";
	setAttr ".wx" -type "double3" 1 0 0 ;
	setAttr ".wy" -type "double3" 0 1 0 ;
createNode joint -n "Ankle" -p "Knee";
	rename -uid "87B804AD-4DA3-5B21-A938-7ABF076202E7";
	addAttr -ci true -sn "n" -ln "name" -dt "string";
	addAttr -ci true -sn "mirror" -ln "mirror" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "ox" -ln "orientX" -min 0 -max 3 -en "Common:Parent:Free:World" 
		-at "enum";
	addAttr -ci true -sn "wx" -ln "worldX" -at "double3" -nc 3;
	addAttr -ci true -sn "wxx" -ln "worldXX" -at "double" -p "worldX";
	addAttr -ci true -sn "wxy" -ln "worldXY" -at "double" -p "worldX";
	addAttr -ci true -sn "wxz" -ln "worldXZ" -at "double" -p "worldX";
	addAttr -ci true -sn "oy" -ln "orientY" -min 0 -max 3 -en "Common:Parent:Free:World" 
		-at "enum";
	addAttr -ci true -sn "wy" -ln "worldY" -at "double3" -nc 3;
	addAttr -ci true -sn "wyx" -ln "worldYX" -at "double" -p "worldY";
	addAttr -ci true -sn "wyy" -ln "worldYY" -at "double" -p "worldY";
	addAttr -ci true -sn "wyz" -ln "worldYZ" -at "double" -p "worldY";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 1 0.4627451 0.45882353 ;
	setAttr ".t" -type "double3" 3.9648628234863281 -1.9627930527254378e-16 -9.7185849862527207e-16 ;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "Foot";
	setAttr ".n" -type "string" "Default";
	setAttr ".wx" -type "double3" 1 0 0 ;
	setAttr ".wy" -type "double3" 0 1 0 ;
createNode joint -n "Toes" -p "Ankle";
	rename -uid "5033B86C-4BE2-FAF4-8796-D08845DA1048";
	addAttr -ci true -sn "n" -ln "name" -dt "string";
	addAttr -ci true -sn "mirror" -ln "mirror" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "ox" -ln "orientX" -min 0 -max 3 -en "Common:Parent:Free:World" 
		-at "enum";
	addAttr -ci true -sn "wx" -ln "worldX" -at "double3" -nc 3;
	addAttr -ci true -sn "wxx" -ln "worldXX" -at "double" -p "worldX";
	addAttr -ci true -sn "wxy" -ln "worldXY" -at "double" -p "worldX";
	addAttr -ci true -sn "wxz" -ln "worldXZ" -at "double" -p "worldX";
	addAttr -ci true -sn "oy" -ln "orientY" -min 0 -max 3 -en "Common:Parent:Free:World" 
		-at "enum";
	addAttr -ci true -sn "wy" -ln "worldY" -at "double3" -nc 3;
	addAttr -ci true -sn "wyx" -ln "worldYX" -at "double" -p "worldY";
	addAttr -ci true -sn "wyy" -ln "worldYY" -at "double" -p "worldY";
	addAttr -ci true -sn "wyz" -ln "worldYZ" -at "double" -p "worldY";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.45490196 0.72549021 1 ;
	setAttr ".t" -type "double3" 0.67734920978546143 1.4452544450759888 0 ;
	setAttr ".jo" -type "double3" -6.6574567395889241e-05 -7.6266146634583427e-05 82.236991315545268 ;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "Child";
	setAttr ".n" -type "string" "Default";
	setAttr ".wx" -type "double3" 1 0 0 ;
	setAttr ".wy" -type "double3" 0 1 0 ;
createNode joint -n "ToesEnd" -p "Toes";
	rename -uid "84C307FD-4095-22E4-F5B5-26A4333D3C4D";
	addAttr -ci true -sn "n" -ln "name" -dt "string";
	addAttr -ci true -sn "mirror" -ln "mirror" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "ox" -ln "orientX" -min 0 -max 3 -en "Common:Parent:Free:World" 
		-at "enum";
	addAttr -ci true -sn "wx" -ln "worldX" -at "double3" -nc 3;
	addAttr -ci true -sn "wxx" -ln "worldXX" -at "double" -p "worldX";
	addAttr -ci true -sn "wxy" -ln "worldXY" -at "double" -p "worldX";
	addAttr -ci true -sn "wxz" -ln "worldXZ" -at "double" -p "worldX";
	addAttr -ci true -sn "oy" -ln "orientY" -min 0 -max 3 -en "Common:Parent:Free:World" 
		-at "enum";
	addAttr -ci true -sn "wy" -ln "worldY" -at "double3" -nc 3;
	addAttr -ci true -sn "wyx" -ln "worldYX" -at "double" -p "worldY";
	addAttr -ci true -sn "wyy" -ln "worldYY" -at "double" -p "worldY";
	addAttr -ci true -sn "wyz" -ln "worldYZ" -at "double" -p "worldY";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 1 1 1 ;
	setAttr ".t" -type "double3" 0.62690100768380419 -1.6993138961474768e-16 2.2204481668326812e-16 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "End";
	setAttr ".n" -type "string" "Default";
	setAttr ".wx" -type "double3" 1 0 0 ;
	setAttr ".wy" -type "double3" 0 1 0 ;
createNode transform -n "Heel_Pivot" -p "Ankle";
	rename -uid "9EF0D60A-43DC-6498-F200-1B8DF613DB05";
	setAttr ".t" -type "double3" 0.84922761464118757 -0.54082792031765015 1.7763568394002505e-15 ;
	setAttr ".r" -type "double3" -89.999999999999986 89.999999999999986 0 ;
	setAttr ".s" -type "double3" 0.99999999999999978 0.99999999999999978 0.99999999999999978 ;
createNode locator -n "Heel_PivotShape" -p "Heel_Pivot";
	rename -uid "819DA190-4B3F-A01C-B8AD-5DB63F1ABDE0";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 1 1 0 ;
	setAttr ".los" -type "double3" 0.1 0.1 0.1 ;
createNode transform -n "Tiptoe_Pivot" -p "Ankle";
	rename -uid "33C3582F-4D09-B256-425F-4DB936F1EB65";
	setAttr ".t" -type "double3" 0.76202842593192943 2.0664100795984259 8.3446502996409322e-07 ;
	setAttr ".r" -type "double3" -89.999999999999986 89.999999999999986 0 ;
	setAttr ".s" -type "double3" 0.99999999999999978 0.99999999999999978 0.99999999999999978 ;
createNode locator -n "Tiptoe_PivotShape" -p "Tiptoe_Pivot";
	rename -uid "B30F5220-4BE5-E133-3568-88A44626B891";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 1 1 0 ;
	setAttr ".los" -type "double3" 0.1 0.1 0.1 ;
createNode transform -n "FootOuter_Pivot" -p "Ankle";
	rename -uid "C8CE6DFC-4058-8B7C-08F2-30997656B145";
	setAttr ".t" -type "double3" 0.85122761464118823 1.4452544450759888 -0.46899999999999986 ;
	setAttr ".r" -type "double3" -89.999999999999986 89.999999999999986 0 ;
	setAttr ".s" -type "double3" 0.99999999999999978 0.99999999999999978 0.99999999999999978 ;
createNode locator -n "FootOuter_PivotShape" -p "FootOuter_Pivot";
	rename -uid "DBB48D77-4495-1D64-8F46-7CA6F3D45AC7";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 1 1 0 ;
	setAttr ".los" -type "double3" 0.1 0.1 0.1 ;
createNode transform -n "FootInner_Pivot" -p "Ankle";
	rename -uid "34C735C0-4016-C6BF-55ED-24BFC39F24A8";
	setAttr ".t" -type "double3" 0.85122761464118823 1.4452544450759888 0.46931465148926055 ;
	setAttr ".r" -type "double3" -89.999999999999986 89.999999999999986 0 ;
	setAttr ".s" -type "double3" 0.99999999999999978 0.99999999999999978 0.99999999999999978 ;
createNode locator -n "FootInner_PivotShape" -p "FootInner_Pivot";
	rename -uid "9A26C57F-4187-01CB-A863-F98BE19696CB";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 1 1 0 ;
	setAttr ".los" -type "double3" 0.1 0.1 0.1 ;
createNode transform -n "Leg_Switch_Pivot" -p "Hip";
	rename -uid "1E4F5725-4FCC-01A5-1F9A-F7A90E3AF51F";
	setAttr ".t" -type "double3" 0.97592177128791668 0 -1.471752050392656 ;
	setAttr ".r" -type "double3" -89.999999999999986 89.999999999999986 0 ;
	setAttr ".s" -type "double3" 0.99999999999999978 0.99999999999999978 0.99999999999999978 ;
createNode locator -n "Leg_Switch_PivotShape" -p "Leg_Switch_Pivot";
	rename -uid "7DB4EE7B-4397-DAE4-EA4D-AEACF12DBAEC";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 1 1 0 ;
	setAttr ".los" -type "double3" 0.1 0.1 0.1 ;
createNode lightLinker -s -n "lightLinker1";
	rename -uid "AD5A9D2E-4AEE-AB81-B35B-64823BA2B45E";
	setAttr -s 2 ".lnk";
	setAttr -s 2 ".slnk";
createNode shapeEditorManager -n "shapeEditorManager";
	rename -uid "9BF7C008-4EBC-4D4A-B000-EABE8F142ED6";
createNode poseInterpolatorManager -n "poseInterpolatorManager";
	rename -uid "FDA0907F-4CDA-ED61-87FD-57A54D8E1EA1";
createNode displayLayerManager -n "layerManager";
	rename -uid "2BA28E82-44CE-CCE0-F1BA-84B5803B72CB";
createNode displayLayer -n "defaultLayer";
	rename -uid "36E4C212-4113-094B-8EB7-AC9F9A4FA817";
createNode renderLayerManager -n "renderLayerManager";
	rename -uid "1F62C17C-40A6-6A45-BDDB-00813688E7C2";
createNode renderLayer -n "defaultRenderLayer";
	rename -uid "71D61A82-40BE-3BDC-3915-979CD75F6E86";
	setAttr ".g" yes;
createNode script -n "uiConfigurationScriptNode";
	rename -uid "0E5F4D0E-4F49-7A98-6766-EFB0187C9976";
	setAttr ".b" -type "string" (
		"// Maya Mel UI Configuration File.\n//\n//  This script is machine generated.  Edit at your own risk.\n//\n//\n\nglobal string $gMainPane;\nif (`paneLayout -exists $gMainPane`) {\n\n\tglobal int $gUseScenePanelConfig;\n\tint    $useSceneConfig = $gUseScenePanelConfig;\n\tint    $menusOkayInPanels = `optionVar -q allowMenusInPanels`;\tint    $nVisPanes = `paneLayout -q -nvp $gMainPane`;\n\tint    $nPanes = 0;\n\tstring $editorName;\n\tstring $panelName;\n\tstring $itemFilterName;\n\tstring $panelConfig;\n\n\t//\n\t//  get current state of the UI\n\t//\n\tsceneUIReplacement -update $gMainPane;\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Top View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Top View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -docTag \"RADRENDER\" \n            -editorChanged \"updateModelPanelBar\" \n            -camera \"top\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n"
		+ "            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 32768\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n"
		+ "            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -controllers 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n"
		+ "            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1\n            -height 1\n            -sceneRenderFilter 0\n            -activeShadingGraph \"ballora_animatronic_shadow_rig:rsMaterial1SG,ballora_animatronic_shadow_rig:MAT_ballora,ballora_animatronic_shadow_rig:MAT_ballora\" \n            -activeCustomGeometry \"meshShaderball\" \n            -activeCustomLighSet \"defaultAreaLightSet\" \n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n"
		+ "            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Side View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Side View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -docTag \"RADRENDER\" \n            -editorChanged \"updateModelPanelBar\" \n            -camera \"side\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n"
		+ "            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 32768\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n"
		+ "            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -controllers 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n"
		+ "            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1079\n            -height 703\n            -sceneRenderFilter 0\n            -activeShadingGraph \"ballora_animatronic_shadow_rig:rsMaterial1SG,ballora_animatronic_shadow_rig:MAT_ballora,ballora_animatronic_shadow_rig:MAT_ballora\" \n            -activeCustomGeometry \"meshShaderball\" \n            -activeCustomLighSet \"defaultAreaLightSet\" \n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Front View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Front View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n"
		+ "        modelEditor -e \n            -docTag \"RADRENDER\" \n            -editorChanged \"updateModelPanelBar\" \n            -camera \"front\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 32768\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n"
		+ "            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -controllers 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n"
		+ "            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1\n            -height 1\n            -sceneRenderFilter 0\n            -activeShadingGraph \"ballora_animatronic_shadow_rig:rsMaterial1SG,ballora_animatronic_shadow_rig:MAT_ballora,ballora_animatronic_shadow_rig:MAT_ballora\" \n            -activeCustomGeometry \"meshShaderball\" \n"
		+ "            -activeCustomLighSet \"defaultAreaLightSet\" \n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Persp View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Persp View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -docTag \"RADRENDER\" \n            -editorChanged \"updateModelPanelBar\" \n            -camera \"persp\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n"
		+ "            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 32768\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n"
		+ "            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -controllers 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n"
		+ "            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1079\n            -height 703\n            -sceneRenderFilter 0\n            -activeShadingGraph \"ballora_animatronic_shadow_rig:rsMaterial1SG,ballora_animatronic_shadow_rig:MAT_ballora,ballora_animatronic_shadow_rig:MAT_ballora\" \n            -activeCustomGeometry \"meshShaderball\" \n            -activeCustomLighSet \"defaultAreaLightSet\" \n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"outlinerPanel\" (localizedPanelLabel(\"\")) `;\n"
		+ "\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\toutlinerPanel -edit -l (localizedPanelLabel(\"\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        outlinerEditor -e \n            -docTag \"isolOutln_fromSeln\" \n            -showShapes 0\n            -showAssignedMaterials 0\n            -showTimeEditor 1\n            -showReferenceNodes 0\n            -showReferenceMembers 0\n            -showAttributes 0\n            -showConnected 0\n            -showAnimCurvesOnly 0\n            -showMuteInfo 0\n            -organizeByLayer 1\n            -organizeByClip 1\n            -showAnimLayerWeight 1\n            -autoExpandLayers 1\n            -autoExpand 0\n            -showDagOnly 1\n            -showAssets 1\n            -showContainedOnly 1\n            -showPublishedAsConnected 0\n            -showParentContainers 0\n            -showContainerContents 1\n            -ignoreDagHierarchy 0\n            -expandConnections 0\n            -showUpstreamCurves 1\n            -showUnitlessCurves 1\n            -showCompounds 1\n"
		+ "            -showLeafs 1\n            -showNumericAttrsOnly 0\n            -highlightActive 1\n            -autoSelectNewObjects 0\n            -doNotSelectNewObjects 0\n            -dropIsParent 1\n            -transmitFilters 0\n            -setFilter \"defaultSetFilter\" \n            -showSetMembers 1\n            -allowMultiSelection 1\n            -alwaysToggleSelect 0\n            -directSelect 0\n            -isSet 0\n            -isSetMember 0\n            -displayMode \"DAG\" \n            -expandObjects 0\n            -setsIgnoreFilters 1\n            -containersIgnoreFilters 0\n            -editAttrName 0\n            -showAttrValues 0\n            -highlightSecondary 0\n            -showUVAttrsOnly 0\n            -showTextureNodesOnly 0\n            -attrAlphaOrder \"default\" \n            -animLayerFilterOptions \"allAffecting\" \n            -sortOrder \"none\" \n            -longNames 0\n            -niceNames 1\n            -selectCommand \"<function selCom at 0x7f29c5c04aa0>\" \n            -showNamespace 1\n            -showPinIcons 0\n"
		+ "            -mapMotionTrails 0\n            -ignoreHiddenAttribute 0\n            -ignoreOutlinerColor 0\n            -renderFilterVisible 0\n            -renderFilterIndex 0\n            -selectionOrder \"chronological\" \n            -expandAttribute 0\n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"outlinerPanel\" (localizedPanelLabel(\"Outliner\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\toutlinerPanel -edit -l (localizedPanelLabel(\"Outliner\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        outlinerEditor -e \n            -docTag \"isolOutln_fromSeln\" \n            -showShapes 0\n            -showAssignedMaterials 0\n            -showTimeEditor 1\n            -showReferenceNodes 0\n            -showReferenceMembers 0\n            -showAttributes 0\n            -showConnected 0\n            -showAnimCurvesOnly 0\n            -showMuteInfo 0\n            -organizeByLayer 1\n            -organizeByClip 1\n"
		+ "            -showAnimLayerWeight 1\n            -autoExpandLayers 1\n            -autoExpand 0\n            -showDagOnly 1\n            -showAssets 1\n            -showContainedOnly 1\n            -showPublishedAsConnected 0\n            -showParentContainers 0\n            -showContainerContents 1\n            -ignoreDagHierarchy 0\n            -expandConnections 0\n            -showUpstreamCurves 1\n            -showUnitlessCurves 1\n            -showCompounds 1\n            -showLeafs 1\n            -showNumericAttrsOnly 0\n            -highlightActive 1\n            -autoSelectNewObjects 0\n            -doNotSelectNewObjects 0\n            -dropIsParent 1\n            -transmitFilters 0\n            -setFilter \"defaultSetFilter\" \n            -showSetMembers 1\n            -allowMultiSelection 1\n            -alwaysToggleSelect 0\n            -directSelect 0\n            -displayMode \"DAG\" \n            -expandObjects 0\n            -setsIgnoreFilters 1\n            -containersIgnoreFilters 0\n            -editAttrName 0\n            -showAttrValues 0\n"
		+ "            -highlightSecondary 0\n            -showUVAttrsOnly 0\n            -showTextureNodesOnly 0\n            -attrAlphaOrder \"default\" \n            -animLayerFilterOptions \"allAffecting\" \n            -sortOrder \"none\" \n            -longNames 0\n            -niceNames 1\n            -showNamespace 1\n            -showPinIcons 0\n            -mapMotionTrails 0\n            -ignoreHiddenAttribute 0\n            -ignoreOutlinerColor 0\n            -renderFilterVisible 0\n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"graphEditor\" (localizedPanelLabel(\"Graph Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Graph Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n                -showShapes 1\n                -showAssignedMaterials 0\n                -showTimeEditor 1\n                -showReferenceNodes 0\n"
		+ "                -showReferenceMembers 0\n                -showAttributes 1\n                -showConnected 1\n                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -organizeByClip 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 1\n                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n                -showParentContainers 1\n                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 1\n                -showCompounds 0\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n                -autoSelectNewObjects 1\n                -doNotSelectNewObjects 0\n                -dropIsParent 1\n                -transmitFilters 1\n                -setFilter \"0\" \n"
		+ "                -showSetMembers 0\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 1\n                -mapMotionTrails 1\n                -ignoreHiddenAttribute 0\n                -ignoreOutlinerColor 0\n                -renderFilterVisible 0\n                $editorName;\n\n\t\t\t$editorName = ($panelName+\"GraphEd\");\n            animCurveEditor -e \n                -displayKeys 1\n                -displayTangents 0\n"
		+ "                -displayActiveKeys 0\n                -displayActiveKeyTangents 1\n                -displayInfinities 0\n                -displayValues 0\n                -autoFit 1\n                -snapTime \"integer\" \n                -snapValue \"none\" \n                -showResults \"off\" \n                -showBufferCurves \"off\" \n                -smoothness \"fine\" \n                -resultSamples 1\n                -resultScreenSamples 0\n                -resultUpdate \"delayed\" \n                -showUpstreamCurves 1\n                -showCurveNames 0\n                -showActiveCurveNames 0\n                -stackedCurves 0\n                -stackedCurvesMin -1\n                -stackedCurvesMax 1\n                -stackedCurvesSpace 0.2\n                -displayNormalized 0\n                -preSelectionHighlight 0\n                -constrainDrag 0\n                -classicMode 1\n                -valueLinesToggle 1\n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dopeSheetPanel\" (localizedPanelLabel(\"Dope Sheet\")) `;\n"
		+ "\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Dope Sheet\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n                -showShapes 1\n                -showAssignedMaterials 0\n                -showTimeEditor 1\n                -showReferenceNodes 0\n                -showReferenceMembers 0\n                -showAttributes 1\n                -showConnected 1\n                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -organizeByClip 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 0\n                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n                -showParentContainers 1\n                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n"
		+ "                -showUpstreamCurves 1\n                -showUnitlessCurves 0\n                -showCompounds 1\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n                -autoSelectNewObjects 0\n                -doNotSelectNewObjects 1\n                -dropIsParent 1\n                -transmitFilters 0\n                -setFilter \"0\" \n                -showSetMembers 0\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n"
		+ "                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 0\n                -mapMotionTrails 1\n                -ignoreHiddenAttribute 0\n                -ignoreOutlinerColor 0\n                -renderFilterVisible 0\n                $editorName;\n\n\t\t\t$editorName = ($panelName+\"DopeSheetEd\");\n            dopeSheetEditor -e \n                -displayKeys 1\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -displayValues 0\n                -autoFit 0\n                -snapTime \"integer\" \n                -snapValue \"none\" \n                -outliner \"dopeSheetPanel1OutlineEd\" \n                -showSummary 1\n                -showScene 0\n                -hierarchyBelow 0\n                -showTicks 1\n                -selectionWindow 0 0 0 0 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"timeEditorPanel\" (localizedPanelLabel(\"Time Editor\")) `;\n"
		+ "\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Time Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"clipEditorPanel\" (localizedPanelLabel(\"Trax Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Trax Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = clipEditorNameFromPanel($panelName);\n            clipEditor -e \n                -displayKeys 0\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -displayValues 0\n                -autoFit 0\n                -snapTime \"none\" \n                -snapValue \"none\" \n                -initialized 0\n                -manageSequencer 0 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n"
		+ "\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"sequenceEditorPanel\" (localizedPanelLabel(\"Camera Sequencer\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Camera Sequencer\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = sequenceEditorNameFromPanel($panelName);\n            clipEditor -e \n                -displayKeys 0\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -displayValues 0\n                -autoFit 0\n                -snapTime \"none\" \n                -snapValue \"none\" \n                -initialized 0\n                -manageSequencer 1 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"hyperGraphPanel\" (localizedPanelLabel(\"Hypergraph Hierarchy\")) `;\n\tif (\"\" != $panelName) {\n"
		+ "\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Hypergraph Hierarchy\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"HyperGraphEd\");\n            hyperGraph -e \n                -graphLayoutStyle \"hierarchicalLayout\" \n                -orientation \"horiz\" \n                -mergeConnections 0\n                -zoom 1\n                -animateTransition 0\n                -showRelationships 1\n                -showShapes 0\n                -showDeformers 0\n                -showExpressions 0\n                -showConstraints 0\n                -showConnectionFromSelected 0\n                -showConnectionToSelected 0\n                -showConstraintLabels 0\n                -showUnderworld 0\n                -showInvisible 0\n                -transitionFrames 1\n                -opaqueContainers 0\n                -freeform 0\n                -imagePosition 0 0 \n                -imageScale 1\n                -imageEnabled 0\n                -graphType \"DAG\" \n                -heatMapDisplay 0\n"
		+ "                -updateSelection 1\n                -updateNodeAdded 1\n                -useDrawOverrideColor 0\n                -limitGraphTraversal -1\n                -range 0 0 \n                -iconSize \"smallIcons\" \n                -showCachedConnections 0\n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"hyperShadePanel\" (localizedPanelLabel(\"Hypershade\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Hypershade\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"visorPanel\" (localizedPanelLabel(\"Visor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Visor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n"
		+ "\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"createNodePanel\" (localizedPanelLabel(\"Create Node\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Create Node\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"polyTexturePlacementPanel\" (localizedPanelLabel(\"UV Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"UV Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"renderWindowPanel\" (localizedPanelLabel(\"Render View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Render View\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n"
		+ "\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"shapePanel\" (localizedPanelLabel(\"Shape Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tshapePanel -edit -l (localizedPanelLabel(\"Shape Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"posePanel\" (localizedPanelLabel(\"Pose Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tposePanel -edit -l (localizedPanelLabel(\"Pose Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dynRelEdPanel\" (localizedPanelLabel(\"Dynamic Relationships\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Dynamic Relationships\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n"
		+ "\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"relationshipPanel\" (localizedPanelLabel(\"Relationship Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Relationship Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"referenceEditorPanel\" (localizedPanelLabel(\"Reference Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Reference Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"componentEditorPanel\" (localizedPanelLabel(\"Component Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Component Editor\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dynPaintScriptedPanelType\" (localizedPanelLabel(\"Paint Effects\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Paint Effects\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"scriptEditorPanel\" (localizedPanelLabel(\"Script Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Script Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"profilerPanel\" (localizedPanelLabel(\"Profiler Tool\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Profiler Tool\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"contentBrowserPanel\" (localizedPanelLabel(\"Content Browser\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Content Browser\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"Stereo\" (localizedPanelLabel(\"Stereo\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Stereo\")) -mbv $menusOkayInPanels  $panelName;\nstring $editorName = ($panelName+\"Editor\");\n            stereoCameraView -e \n                -camera \"persp\" \n                -useInteractiveMode 0\n                -displayLights \"default\" \n                -displayAppearance \"smoothShaded\" \n                -activeOnly 0\n                -ignorePanZoom 0\n                -wireframeOnShaded 0\n"
		+ "                -headsUpDisplay 1\n                -holdOuts 1\n                -selectionHiliteDisplay 1\n                -useDefaultMaterial 0\n                -bufferMode \"double\" \n                -twoSidedLighting 0\n                -backfaceCulling 0\n                -xray 0\n                -jointXray 0\n                -activeComponentsXray 0\n                -displayTextures 0\n                -smoothWireframe 0\n                -lineWidth 1\n                -textureAnisotropic 0\n                -textureHilight 1\n                -textureSampling 2\n                -textureDisplay \"modulate\" \n                -textureMaxSize 32768\n                -fogging 0\n                -fogSource \"fragment\" \n                -fogMode \"linear\" \n                -fogStart 0\n                -fogEnd 100\n                -fogDensity 0.1\n                -fogColor 0.5 0.5 0.5 1 \n                -depthOfFieldPreview 1\n                -maxConstantTransparency 1\n                -objectFilterShowInHUD 1\n                -isFiltered 0\n                -colorResolution 4 4 \n"
		+ "                -bumpResolution 4 4 \n                -textureCompression 0\n                -transparencyAlgorithm \"frontAndBackCull\" \n                -transpInShadows 0\n                -cullingOverride \"none\" \n                -lowQualityLighting 0\n                -maximumNumHardwareLights 0\n                -occlusionCulling 0\n                -shadingModel 0\n                -useBaseRenderer 0\n                -useReducedRenderer 0\n                -smallObjectCulling 0\n                -smallObjectThreshold -1 \n                -interactiveDisableShadows 0\n                -interactiveBackFaceCull 0\n                -sortTransparent 1\n                -controllers 1\n                -nurbsCurves 1\n                -nurbsSurfaces 1\n                -polymeshes 1\n                -subdivSurfaces 1\n                -planes 1\n                -lights 1\n                -cameras 1\n                -controlVertices 1\n                -hulls 1\n                -grid 1\n                -imagePlane 1\n                -joints 1\n                -ikHandles 1\n"
		+ "                -deformers 1\n                -dynamics 1\n                -particleInstancers 1\n                -fluids 1\n                -hairSystems 1\n                -follicles 1\n                -nCloths 1\n                -nParticles 1\n                -nRigids 1\n                -dynamicConstraints 1\n                -locators 1\n                -manipulators 1\n                -pluginShapes 1\n                -dimensions 1\n                -handles 1\n                -pivots 1\n                -textures 1\n                -strokes 1\n                -motionTrails 1\n                -clipGhosts 1\n                -greasePencils 1\n                -shadows 0\n                -captureSequenceNumber -1\n                -width 0\n                -height 0\n                -sceneRenderFilter 0\n                -displayMode \"centerEye\" \n                -viewColor 0 0 0 1 \n                -useCustomBackground 1\n                $editorName;\n            stereoCameraView -e -viewSelected 0 $editorName;\n            stereoCameraView -e \n"
		+ "                -pluginObjects \"gpuCacheDisplayFilter\" 1 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"outlinerPanel\" (localizedPanelLabel(\"ToggledOutliner\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\toutlinerPanel -edit -l (localizedPanelLabel(\"ToggledOutliner\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        outlinerEditor -e \n            -showShapes 0\n            -showAssignedMaterials 0\n            -showTimeEditor 1\n            -showReferenceNodes 1\n            -showReferenceMembers 1\n            -showAttributes 0\n            -showConnected 0\n            -showAnimCurvesOnly 0\n            -showMuteInfo 0\n            -organizeByLayer 1\n            -organizeByClip 1\n            -showAnimLayerWeight 1\n            -autoExpandLayers 1\n            -autoExpand 0\n            -showDagOnly 1\n            -showAssets 1\n            -showContainedOnly 1\n            -showPublishedAsConnected 0\n"
		+ "            -showParentContainers 0\n            -showContainerContents 1\n            -ignoreDagHierarchy 0\n            -expandConnections 0\n            -showUpstreamCurves 1\n            -showUnitlessCurves 1\n            -showCompounds 1\n            -showLeafs 1\n            -showNumericAttrsOnly 0\n            -highlightActive 1\n            -autoSelectNewObjects 0\n            -doNotSelectNewObjects 0\n            -dropIsParent 1\n            -transmitFilters 0\n            -setFilter \"defaultSetFilter\" \n            -showSetMembers 1\n            -allowMultiSelection 1\n            -alwaysToggleSelect 0\n            -directSelect 0\n            -isSet 0\n            -isSetMember 0\n            -displayMode \"DAG\" \n            -expandObjects 0\n            -setsIgnoreFilters 1\n            -containersIgnoreFilters 0\n            -editAttrName 0\n            -showAttrValues 0\n            -highlightSecondary 0\n            -showUVAttrsOnly 0\n            -showTextureNodesOnly 0\n            -attrAlphaOrder \"default\" \n            -animLayerFilterOptions \"allAffecting\" \n"
		+ "            -sortOrder \"none\" \n            -longNames 0\n            -niceNames 1\n            -showNamespace 1\n            -showPinIcons 0\n            -mapMotionTrails 0\n            -ignoreHiddenAttribute 0\n            -ignoreOutlinerColor 0\n            -renderFilterVisible 0\n            -renderFilterIndex 0\n            -selectionOrder \"chronological\" \n            -expandAttribute 0\n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"nodeEditorPanel\" (localizedPanelLabel(\"Node Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Node Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"NodeEditorEd\");\n            nodeEditor -e \n                -allAttributes 0\n                -allNodes 0\n                -autoSizeNodes 1\n                -consistentNameSize 1\n                -createNodeCommand \"nodeEdCreateNodeCommand\" \n"
		+ "                -connectNodeOnCreation 0\n                -connectOnDrop 0\n                -highlightConnections 0\n                -copyConnectionsOnPaste 0\n                -defaultPinnedState 0\n                -additiveGraphingMode 0\n                -settingsChangedCallback \"nodeEdSyncControls\" \n                -traversalDepthLimit -1\n                -keyPressCommand \"nodeEdKeyPressCommand\" \n                -nodeTitleMode \"name\" \n                -gridSnap 0\n                -gridVisibility 1\n                -crosshairOnEdgeDragging 0\n                -popupMenuScript \"nodeEdBuildPanelMenus\" \n                -showNamespace 1\n                -showShapes 1\n                -showSGShapes 0\n                -showTransforms 1\n                -useAssets 1\n                -syncedSelection 1\n                -extendToShapes 1\n                -activeTab -1\n                -editorMode \"default\" \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\tif ($useSceneConfig) {\n        string $configName = `getPanel -cwl (localizedPanelLabel(\"Current Layout\"))`;\n"
		+ "        if (\"\" != $configName) {\n\t\t\tpanelConfiguration -edit -label (localizedPanelLabel(\"Current Layout\")) \n\t\t\t\t-userCreated false\n\t\t\t\t-defaultImage \"\"\n\t\t\t\t-image \"\"\n\t\t\t\t-sc false\n\t\t\t\t-configString \"global string $gMainPane; paneLayout -e -cn \\\"single\\\" -ps 1 100 100 $gMainPane;\"\n\t\t\t\t-removeAllPanels\n\t\t\t\t-ap false\n\t\t\t\t\t(localizedPanelLabel(\"Persp View\")) \n\t\t\t\t\t\"modelPanel\"\n"
		+ "\t\t\t\t\t\"$panelName = `modelPanel -unParent -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels `;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -docTag \\\"RADRENDER\\\" \\n    -editorChanged \\\"updateModelPanelBar\\\" \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 0\\n    -headsUpDisplay 1\\n    -holdOuts 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 0\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 0\\n    -activeComponentsXray 0\\n    -displayTextures 0\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 32768\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -depthOfFieldPreview 1\\n    -maxConstantTransparency 1\\n    -rendererName \\\"vp2Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -controllers 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -particleInstancers 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -greasePencils 1\\n    -shadows 0\\n    -captureSequenceNumber -1\\n    -width 1079\\n    -height 703\\n    -sceneRenderFilter 0\\n    -activeShadingGraph \\\"ballora_animatronic_shadow_rig:rsMaterial1SG,ballora_animatronic_shadow_rig:MAT_ballora,ballora_animatronic_shadow_rig:MAT_ballora\\\" \\n    -activeCustomGeometry \\\"meshShaderball\\\" \\n    -activeCustomLighSet \\\"defaultAreaLightSet\\\" \\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName;\\nmodelEditor -e \\n    -pluginObjects \\\"gpuCacheDisplayFilter\\\" 1 \\n    $editorName\"\n"
		+ "\t\t\t\t\t\"modelPanel -edit -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels  $panelName;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -docTag \\\"RADRENDER\\\" \\n    -editorChanged \\\"updateModelPanelBar\\\" \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 0\\n    -headsUpDisplay 1\\n    -holdOuts 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 0\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 0\\n    -activeComponentsXray 0\\n    -displayTextures 0\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 32768\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -depthOfFieldPreview 1\\n    -maxConstantTransparency 1\\n    -rendererName \\\"vp2Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -controllers 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -particleInstancers 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -greasePencils 1\\n    -shadows 0\\n    -captureSequenceNumber -1\\n    -width 1079\\n    -height 703\\n    -sceneRenderFilter 0\\n    -activeShadingGraph \\\"ballora_animatronic_shadow_rig:rsMaterial1SG,ballora_animatronic_shadow_rig:MAT_ballora,ballora_animatronic_shadow_rig:MAT_ballora\\\" \\n    -activeCustomGeometry \\\"meshShaderball\\\" \\n    -activeCustomLighSet \\\"defaultAreaLightSet\\\" \\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName;\\nmodelEditor -e \\n    -pluginObjects \\\"gpuCacheDisplayFilter\\\" 1 \\n    $editorName\"\n"
		+ "\t\t\t\t$configName;\n\n            setNamedPanelLayout (localizedPanelLabel(\"Current Layout\"));\n        }\n\n        panelHistory -e -clear mainPanelHistory;\n        sceneUIReplacement -clear;\n\t}\n\n\ngrid -spacing 5 -size 12 -divisions 5 -displayAxes yes -displayGridLines yes -displayDivisionLines yes -displayPerspectiveLabels no -displayOrthographicLabels no -displayAxesBold yes -perspectiveLabelPosition axis -orthographicLabelPosition edge;\nviewManip -drawCompass 0 -compassAngle 0 -frontParameters \"\" -homeParameters \"\" -selectionLockParameters \"\";\n}\n");
	setAttr ".st" 3;
createNode script -n "sceneConfigurationScriptNode";
	rename -uid "2616AE26-4E0A-1F1F-2A1E-47AFF0543BD5";
	setAttr ".b" -type "string" "playbackOptions -min 1 -max 120 -ast 1 -aet 200 ";
	setAttr ".st" 6;
createNode nodeGraphEditorInfo -n "MayaNodeEditorSavedTabsInfo";
	rename -uid "13C7AB66-45C1-60EB-D3CF-1D8CB985AED0";
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -535.71426442691347 -173.8095169029541 ;
	setAttr ".tgi[0].vh" -type "double2" 688.0952107527911 441.66664911641089 ;
	setAttr -s 2 ".tgi[0].ni";
	setAttr ".tgi[0].ni[0].x" -282.14285278320313;
	setAttr ".tgi[0].ni[0].y" 146.42855834960938;
	setAttr ".tgi[0].ni[0].nvs" 18304;
	setAttr ".tgi[0].ni[1].x" -28.571418762207031;
	setAttr ".tgi[0].ni[1].y" 158.33332824707031;
	setAttr ".tgi[0].ni[1].nvs" 18304;
select -ne :time1;
	setAttr -av -k on ".cch";
	setAttr -k on ".fzn";
	setAttr -av -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k on ".o" 1;
	setAttr -av -k on ".unw" 1;
	setAttr -av -k on ".etw";
	setAttr -av -k on ".tps";
	setAttr -av -k on ".tms";
select -ne :hardwareRenderingGlobals;
	setAttr -av -k on ".cch";
	setAttr -av -k on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr ".otfna" -type "stringArray" 22 "NURBS Curves" "NURBS Surfaces" "Polygons" "Subdiv Surface" "Particles" "Particle Instance" "Fluids" "Strokes" "Image Planes" "UI" "Lights" "Cameras" "Locators" "Joints" "IK Handles" "Deformers" "Motion Trails" "Components" "Hair Systems" "Follicles" "Misc. UI" "Ornaments"  ;
	setAttr ".otfva" -type "Int32Array" 22 0 1 1 1 1 1
		 1 1 1 0 0 0 0 0 0 0 0 0
		 0 0 0 0 ;
	setAttr -k on ".hwi";
	setAttr -av ".ta";
	setAttr -av ".tq";
	setAttr -av ".etmr";
	setAttr -av ".tmr";
	setAttr -av ".aoon";
	setAttr -av ".aoam";
	setAttr -av ".aora";
	setAttr -k on ".hff";
	setAttr -av -k on ".hfd";
	setAttr -av -k on ".hfs";
	setAttr -av -k on ".hfe";
	setAttr -av ".hfc";
	setAttr -av -k on ".hfcr";
	setAttr -av -k on ".hfcg";
	setAttr -av -k on ".hfcb";
	setAttr -av -k on ".hfa";
	setAttr -av ".mbe";
	setAttr -av -k on ".mbsof";
	setAttr -k on ".blen";
	setAttr -k on ".blat";
	setAttr -av ".msaa";
	setAttr ".fprt" yes;
select -ne :renderPartition;
	setAttr -av -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 2 ".st";
	setAttr -cb on ".an";
	setAttr -cb on ".pt";
select -ne :renderGlobalsList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
select -ne :defaultShaderList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 4 ".s";
select -ne :postProcessList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 2 ".p";
select -ne :defaultRenderingList1;
	setAttr -k on ".ihi";
select -ne :initialShadingGroup;
	setAttr -av -k on ".cch";
	setAttr -k on ".fzn";
	setAttr -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k on ".bbx";
	setAttr -k on ".vwm";
	setAttr -k on ".tpv";
	setAttr -k on ".uit";
	setAttr -k on ".mwc";
	setAttr -cb on ".an";
	setAttr -cb on ".il";
	setAttr -cb on ".vo";
	setAttr -cb on ".eo";
	setAttr -cb on ".fo";
	setAttr -cb on ".epo";
	setAttr ".ro" yes;
select -ne :initialParticleSE;
	setAttr -av -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k on ".mwc";
	setAttr -cb on ".an";
	setAttr -cb on ".il";
	setAttr -cb on ".vo";
	setAttr -cb on ".eo";
	setAttr -cb on ".fo";
	setAttr -cb on ".epo";
	setAttr ".ro" yes;
select -ne :defaultResolution;
	setAttr -av -k on ".cch";
	setAttr -av -k on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -k on ".bnm";
	setAttr -av -k on ".w";
	setAttr -av -k on ".h";
	setAttr -av ".pa" 1;
	setAttr -av -k on ".al";
	setAttr -av -k on ".dar";
	setAttr -av -k on ".ldar";
	setAttr -av -k on ".dpi";
	setAttr -av -k on ".off";
	setAttr -av -k on ".fld";
	setAttr -av -k on ".zsl";
	setAttr -av -k on ".isu";
	setAttr -av -k on ".pdu";
select -ne :hardwareRenderGlobals;
	setAttr -av -k on ".cch";
	setAttr -av -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -av ".ctrs" 256;
	setAttr -av ".btrs" 512;
	setAttr -av -k off -cb on ".fbfm";
	setAttr -av -k off -cb on ".ehql";
	setAttr -av -k off -cb on ".eams";
	setAttr -av -k off -cb on ".eeaa";
	setAttr -av -k off -cb on ".engm";
	setAttr -av -k off -cb on ".mes";
	setAttr -av -k off -cb on ".emb";
	setAttr -av -k off -cb on ".mbbf";
	setAttr -av -k off -cb on ".mbs";
	setAttr -av -k off -cb on ".trm";
	setAttr -av -k off -cb on ".tshc";
	setAttr -av -k off -cb on ".enpt";
	setAttr -av -k off -cb on ".clmt";
	setAttr -av -k off -cb on ".tcov";
	setAttr -av -k off -cb on ".lith";
	setAttr -av -k off -cb on ".sobc";
	setAttr -av -k off -cb on ".cuth";
	setAttr -av -k off -cb on ".hgcd";
	setAttr -av -k off -cb on ".hgci";
	setAttr -av -k off -cb on ".mgcs";
	setAttr -av -k off -cb on ".twa";
	setAttr -av -k off -cb on ".twz";
	setAttr -av -k on ".hwcc";
	setAttr -av -k on ".hwdp";
	setAttr -av -k on ".hwql";
	setAttr -av -k on ".hwfr";
	setAttr -av -k on ".soll";
	setAttr -av -k on ".sosl";
	setAttr -av -k on ".bswa";
	setAttr -av -k on ".shml";
	setAttr -av -k on ".hwel";
connectAttr "Block.rigScale" "Block.sx" -l on;
connectAttr "Block.rigScale" "Block.sy" -l on;
connectAttr "Block.rigScale" "Block.sz" -l on;
connectAttr "Root.s" "Spine.is";
connectAttr "Spine.s" "Chest.is";
connectAttr "Chest.s" "Neck.is";
connectAttr "Neck.s" "Head.is";
connectAttr "Head.s" "HeadEnd.is";
connectAttr "Head.s" "Eye.is";
connectAttr "Eye.s" "EyeEnd.is";
connectAttr "Head.s" "Jaw.is";
connectAttr "Jaw.s" "JawEnd.is";
connectAttr "Chest.s" "Scapula.is";
connectAttr "Scapula.s" "Shoulder.is";
connectAttr "Shoulder.s" "Elbow.is";
connectAttr "Elbow.s" "Wrist.is";
connectAttr "Wrist.s" "WristEnd.is";
connectAttr "Wrist.s" "PinkyFinger1.is";
connectAttr "PinkyFinger1.s" "PinkyFinger2.is";
connectAttr "PinkyFinger2.s" "PinkyFinger3.is";
connectAttr "PinkyFinger3.s" "PinkyFingerEnd.is";
connectAttr "Wrist.s" "RingFinger1.is";
connectAttr "RingFinger1.s" "RingFinger2.is";
connectAttr "RingFinger2.s" "RingFinger3.is";
connectAttr "RingFinger3.s" "RingFingerEnd.is";
connectAttr "Wrist.s" "MiddleFinger1.is";
connectAttr "MiddleFinger1.s" "MiddleFinge2.is";
connectAttr "MiddleFinge2.s" "MiddleFinger3.is";
connectAttr "MiddleFinger3.s" "MiddleFingerEnd.is";
connectAttr "Wrist.s" "IndexFinger1.is";
connectAttr "IndexFinger1.s" "IndexFinger2.is";
connectAttr "IndexFinger2.s" "IndexFinger3.is";
connectAttr "IndexFinger3.s" "IndexFingerEnd.is";
connectAttr "Wrist.s" "ThumbFinger1.is";
connectAttr "ThumbFinger1.s" "ThumbFinger2.is";
connectAttr "ThumbFinger2.s" "ThumbFinger3.is";
connectAttr "ThumbFinger3.s" "ThumbFingerEnd.is";
connectAttr "Root.s" "Hip.is";
connectAttr "Hip.s" "Knee.is";
connectAttr "Knee.s" "Ankle.is";
connectAttr "Ankle.s" "Toes.is";
connectAttr "Toes.s" "ToesEnd.is";
relationship "link" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
connectAttr "layerManager.dli[0]" "defaultLayer.id";
connectAttr "renderLayerManager.rlmi[0]" "defaultRenderLayer.rlid";
connectAttr "BlockShape.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[0].dn";
connectAttr "Block.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[1].dn";
connectAttr "defaultRenderLayer.msg" ":defaultRenderingList1.r" -na;
// End of my2.ma
