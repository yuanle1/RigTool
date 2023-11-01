//Maya ASCII 2018 scene
//Name: my3.ma
//Last modified: Mon, Oct 09, 2023 02:31:35 PM
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
	setAttr ".t" -type "double3" 10.243648422402336 25.979644221737122 7.7729333866793038 ;
	setAttr ".r" -type "double3" -51.938352729930685 372.59999999934308 8.1476074740659888e-16 ;
createNode camera -s -n "perspShape" -p "persp";
	rename -uid "25FF0A99-478C-B96B-7831-949F6E2EB352";
	setAttr -k off ".v" no;
	setAttr ".fl" 34.999999999999993;
	setAttr ".coi" 22.101968493084371;
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
createNode transform -n "back";
	rename -uid "BC36FB17-4FA6-63F4-39F7-61B11B46497B";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 0 -1000.1 ;
	setAttr ".r" -type "double3" 0 180 0 ;
createNode camera -n "backShape" -p "back";
	rename -uid "E3BF2C29-4F10-5136-4F77-5E861A1EBC63";
	setAttr -k off ".v";
	setAttr ".rnd" no;
	setAttr ".coi" 1000.1;
	setAttr ".ow" 9.896330088931947;
	setAttr ".imn" -type "string" "back1";
	setAttr ".den" -type "string" "back1_depth";
	setAttr ".man" -type "string" "back1_mask";
	setAttr ".hc" -type "string" "viewSet -b %camera";
	setAttr ".o" yes;
	setAttr ".ai_translator" -type "string" "orthographic";
createNode transform -n "Block";
	rename -uid "F1C5B344-4B97-4BF2-CA21-91853F599CA8";
	addAttr -ci true -sn "rigScale" -ln "rigScale" -dv 1 -min 0 -at "double";
	addAttr -ci true -sn "n" -ln "name" -dt "string";
	addAttr -ci true -sn "mainCount" -ln "mainCount" -dv 1 -at "long";
	addAttr -ci true -sn "rootControl" -ln "rootControl" -dv 1 -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "gravityControl" -ln "gravityControl" -dv 1 -min 0 -max 1 -at "bool";
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
	setAttr ".n" -type "string" "Main";
createNode nurbsCurve -n "BlockShape" -p "Block";
	rename -uid "EDB68575-452E-606C-2E79-728E5887871F";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0 0.7098 0.53330004 ;
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
	addAttr -ci true -sn "fat" -ln "fat" -dv 1 -min 0 -at "double";
	addAttr -ci true -sn "subdivide" -ln "subdivide" -at "long";
	addAttr -ci true -sn "n" -ln "name" -dt "string";
	addAttr -ci true -sn "secControl" -ln "secondControl" -dv 1 -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "splineShape" -ln "splineShape" -min 0 -max 5 -en "FK:IK:Spline:Finger:Root:Main" 
		-at "enum";
	addAttr -ci true -sn "secShape" -ln "secShape" -min 0 -max 2 -en "FKSec:IKSec:SplineSec" 
		-at "enum";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.99215686 0.79607844 0.43137255 ;
	setAttr ".t" -type "double3" 1.9709482594718226e-16 9.8285102844238281 0 ;
	setAttr ".r" -type "double3" 3.4986101496098694e-14 6.3611093629270367e-15 -3.180554681463516e-15 ;
	setAttr ".jo" -type "double3" -89.999999999999986 0 89.999999999999986 ;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "Spline";
	setAttr ".wx" -type "double3" 1 0 0 ;
	setAttr ".wy" -type "double3" 0 1 0 ;
	setAttr ".fat" 0.60000000000000009;
	setAttr ".subdivide" 2;
	setAttr ".n" -type "string" "Spine";
	setAttr ".splineShape" 2;
	setAttr ".secShape" 2;
createNode joint -n "Spine" -p "Root";
	rename -uid "7EA14B72-46D4-F729-B979-8E8AE5406450";
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
	addAttr -ci true -sn "fat" -ln "fat" -dv 1 -min 0 -at "double";
	addAttr -ci true -sn "subdivide" -ln "subdivide" -at "long";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.99215686 0.79607844 0.43137255 ;
	setAttr ".t" -type "double3" 1.7560000419616699 9.7477583891429349e-17 -3.899103355657174e-16 ;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "Child";
	setAttr ".wx" -type "double3" 1 0 0 ;
	setAttr ".wy" -type "double3" 0 1 0 ;
	setAttr ".fat" 0.60000000000000009;
	setAttr ".subdivide" 2;
createNode joint -n "Chest" -p "Spine";
	rename -uid "743BB571-49E3-34AD-BC40-E5B847AF8071";
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
	addAttr -ci true -sn "fat" -ln "fat" -dv 1 -min 0 -at "double";
	addAttr -ci true -sn "subdivide" -ln "subdivide" -at "long";
	addAttr -ci true -sn "n" -ln "name" -dt "string";
	addAttr -ci true -sn "segScaleComp" -ln "segScaleComp" -dv 1 -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "secControl" -ln "secondControl" -dv 1 -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fkShape" -ln "fkShape" -min 0 -max 5 -en "FK:IK:Spline:Finger:Root:Main" 
		-at "enum";
	addAttr -ci true -sn "secShape" -ln "secShape" -min 0 -max 2 -en "FKSec:IKSec:SplineSec" 
		-at "enum";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.45490196 0.72549021 1 ;
	setAttr ".t" -type "double3" 1.4259999990463257 -6.1629758220391547e-32 -3.9443045261050599e-31 ;
	setAttr ".r" -type "double3" 1.2722218725854067e-14 -3.5311250384401278e-31 3.1805546814635168e-15 ;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "FK";
	setAttr ".wx" -type "double3" 1 0 0 ;
	setAttr ".wy" -type "double3" 0 1 0 ;
	setAttr ".fat" 0.60000000000000009;
	setAttr ".n" -type "string" "";
createNode joint -n "Neck" -p "Chest";
	rename -uid "21AFE1EF-496D-3FCF-7876-FE8EA1411A18";
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
	addAttr -ci true -sn "fat" -ln "fat" -dv 1 -min 0 -at "double";
	addAttr -ci true -sn "subdivide" -ln "subdivide" -at "long";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.45490196 0.72549021 1 ;
	setAttr ".t" -type "double3" 1.4493891000747681 -1.8203073871823623e-17 5.1696068514710155e-17 ;
	setAttr ".r" -type "double3" 1.4124500153760508e-30 -1.2722218725854067e-14 -1.2722218725854067e-14 ;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "Child";
	setAttr ".wx" -type "double3" 1 0 0 ;
	setAttr ".wy" -type "double3" 0 1 0 ;
	setAttr ".fat" 0.40000000000000013;
createNode joint -n "Head" -p "Neck";
	rename -uid "604979B2-44C1-2C1C-34FB-C5BE5A78BD67";
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
	addAttr -ci true -sn "fat" -ln "fat" -dv 1 -min 0 -at "double";
	addAttr -ci true -sn "subdivide" -ln "subdivide" -at "long";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.45490196 0.72549021 1 ;
	setAttr ".t" -type "double3" 1.2020894289016724 -9.5525009166246901e-18 2.4267718931962319e-16 ;
	setAttr ".r" -type "double3" 3.4986101496098694e-14 -3.1805546814635128e-15 -1.590277340731759e-14 ;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "Child";
	setAttr ".wx" -type "double3" 1 0 0 ;
	setAttr ".wy" -type "double3" 0 1 0 ;
	setAttr ".fat" 0.40000000000000013;
createNode joint -n "HeadEnd" -p "Head";
	rename -uid "E964468B-48CC-BEAD-EB53-F8ADBFB4C980";
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
	addAttr -ci true -sn "fat" -ln "fat" -dv 1 -min 0 -at "double";
	addAttr -ci true -sn "subdivide" -ln "subdivide" -at "long";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 1 1 1 ;
	setAttr ".t" -type "double3" 1.5170962810516357 -5.5511151231257827e-17 1.6843152217967236e-16 ;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "End";
	setAttr ".wx" -type "double3" 1 0 0 ;
	setAttr ".wy" -type "double3" 0 1 0 ;
createNode joint -n "Eye" -p "Head";
	rename -uid "50EF63CA-4651-4A09-C0EC-AB8D4AB094D8";
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
	addAttr -ci true -sn "fat" -ln "fat" -dv 1 -min 0 -at "double";
	addAttr -ci true -sn "subdivide" -ln "subdivide" -at "long";
	addAttr -ci true -sn "segScaleComp" -ln "segScaleComp" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.7764706 0.627451 0.90196079 ;
	setAttr ".t" -type "double3" 0.23521468043327332 -1.1152639389038086 -0.40199345350265503 ;
	setAttr ".r" -type "double3" 0 2.5444437451708134e-14 0 ;
	setAttr ".jo" -type "double3" 1.2722218725854067e-14 1.5775551220059043e-12 -90 ;
	setAttr ".sd" 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "Aim";
	setAttr ".mirror" yes;
	setAttr ".wx" -type "double3" 1 0 0 ;
	setAttr ".wy" -type "double3" 0 1 0 ;
	setAttr ".fat" 0.20000000000000015;
createNode joint -n "EyeEnd" -p "Eye";
	rename -uid "19E0E9B7-4E27-2129-7747-55BFE137BA9C";
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
	addAttr -ci true -sn "fat" -ln "fat" -dv 1 -min 0 -at "double";
	addAttr -ci true -sn "subdivide" -ln "subdivide" -at "long";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 1 1 1 ;
	setAttr ".t" -type "double3" 0.19217437505722046 0 -5.3290705182007514e-15 ;
	setAttr ".jo" -type "double3" 1.2722218725854067e-14 1.5775551220059043e-12 -1.2722218725853717e-14 ;
	setAttr ".sd" 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "End";
	setAttr ".mirror" yes;
	setAttr ".wx" -type "double3" 1 0 0 ;
	setAttr ".wy" -type "double3" 0 1 0 ;
createNode joint -n "Jaw" -p "Head";
	rename -uid "70D24F83-4AB4-1715-C2AD-A6B386BE3314";
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
	addAttr -ci true -sn "fat" -ln "fat" -dv 1 -min 0 -at "double";
	addAttr -ci true -sn "subdivide" -ln "subdivide" -at "long";
	setAttr ".v" no;
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.45490196 0.72549021 1 ;
	setAttr ".t" -type "double3" -0.28607422113418579 -0.41421523690223694 -1.3813750793513052e-17 ;
	setAttr ".jo" -type "double3" 2.5444437451708134e-14 179.99999999999997 65.082270012640791 ;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "Child";
	setAttr ".wx" -type "double3" 1 0 0 ;
	setAttr ".wy" -type "double3" 0 1 0 ;
	setAttr ".fat" 0.40000000000000013;
createNode joint -n "JawEnd" -p "Jaw";
	rename -uid "84BFA510-4137-1AE6-A347-C8A8439D4812";
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
	addAttr -ci true -sn "fat" -ln "fat" -dv 1 -min 0 -at "double";
	addAttr -ci true -sn "subdivide" -ln "subdivide" -at "long";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 1 1 1 ;
	setAttr ".t" -type "double3" 1.1019491704022375 -1.7763568394002505e-15 -4.4859546570605246e-16 ;
	setAttr ".jo" -type "double3" 2.9620253310164901e-14 -4.2416221355294173e-15 -1.272221872585407e-14 ;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "End";
	setAttr ".wx" -type "double3" 1 0 0 ;
	setAttr ".wy" -type "double3" 0 1 0 ;
createNode joint -n "Scapula" -p "Chest";
	rename -uid "1CEF013D-4C80-07ED-59FB-4C9A0ADA84E8";
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
	addAttr -ci true -sn "fat" -ln "fat" -dv 1 -min 0 -at "double";
	addAttr -ci true -sn "subdivide" -ln "subdivide" -at "long";
	addAttr -ci true -sn "n" -ln "name" -dt "string";
	addAttr -ci true -sn "segScaleComp" -ln "segScaleComp" -dv 1 -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "secControl" -ln "secondControl" -dv 1 -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fkShape" -ln "fkShape" -min 0 -max 5 -en "FK:IK:Spline:Finger:Root:Main" 
		-at "enum";
	addAttr -ci true -sn "secShape" -ln "secShape" -min 0 -max 2 -en "FKSec:IKSec:SplineSec" 
		-at "enum";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 0.45490196 0.72549021 1 ;
	setAttr ".t" -type "double3" 0.68687349557876587 -2.7755575615628914e-16 -0.48817041516304016 ;
	setAttr ".r" -type "double3" -1.1343304013543187e-29 -3.6053389458130899e-14 3.6053389458130905e-14 ;
	setAttr ".jo" -type "double3" 1.2722218725854064e-14 89.999999999999986 0 ;
	setAttr ".sd" 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "FK";
	setAttr ".mirror" yes;
	setAttr ".wx" -type "double3" 1 0 0 ;
	setAttr ".wy" -type "double3" 0 1 0 ;
	setAttr ".fat" 0.6;
	setAttr ".n" -type "string" "";
createNode joint -n "Shoulder" -p "Scapula";
	rename -uid "3D7AED4B-496E-A834-238D-B3B232EC2FB4";
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
	addAttr -ci true -sn "fat" -ln "fat" -dv 1 -min 0 -at "double";
	addAttr -ci true -sn "subdivide" -ln "subdivide" -at "long";
	addAttr -ci true -sn "n" -ln "name" -dt "string";
	addAttr -ci true -sn "segScaleComp" -ln "segScaleComp" -dv 1 -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "secControl" -ln "secondControl" -dv 1 -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "ikShape" -ln "ikShape" -min 0 -max 5 -en "FK:IK:Spline:Finger:Root:Main" 
		-at "enum";
	addAttr -ci true -sn "fkShape" -ln "fkShape" -min 0 -max 5 -en "FK:IK:Spline:Finger:Root:Main" 
		-at "enum";
	addAttr -ci true -sn "secShape" -ln "secShape" -min 0 -max 2 -en "FKSec:IKSec:SplineSec" 
		-at "enum";
	addAttr -ci true -sn "switchPivot" -ln "switchPivot" -dt "string";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 1 0.4627451 0.45882353 ;
	setAttr ".t" -type "double3" 0.95341253280639637 3.882350632147261e-16 0 ;
	setAttr ".jo" -type "double3" 1.272221872585407e-14 0 3.3379600780081558 ;
	setAttr ".sd" 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "IK";
	setAttr ".mirror" yes;
	setAttr ".wx" -type "double3" 1 0 0 ;
	setAttr ".wy" -type "double3" 0 1 0 ;
	setAttr ".fat" 0.50000000000000011;
	setAttr ".subdivide" 2;
	setAttr ".n" -type "string" "Arm";
	setAttr ".secShape" 1;
	setAttr ".switchPivot" -type "string" "";
createNode transform -n "Arm_Switch_Pivot" -p "Shoulder";
	rename -uid "E5E97128-456E-70ED-D75A-50A41731F558";
	setAttr ".t" -type "double3" 1.1694837539124776 0 0.83482051236944699 ;
	setAttr ".rp" -type "double3" 0 -1.3877787807814457e-17 0 ;
	setAttr ".sp" -type "double3" 0 -1.3877787807814457e-17 0 ;
createNode locator -n "Arm_Switch_PivotShape" -p "Arm_Switch_Pivot";
	rename -uid "AB0258C5-4D60-0104-8AB4-FFA8C437DE77";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 1 1 0 ;
	setAttr ".lp" -type "double3" 0 -1.3563304560651781e-17 -1.7763568394002505e-15 ;
	setAttr ".los" -type "double3" 0.1 0.1 0.1 ;
createNode joint -n "Elbow" -p "Shoulder";
	rename -uid "5CD9CAD5-4D17-4178-5DC5-209ECCDB72DE";
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
	addAttr -ci true -sn "fat" -ln "fat" -dv 1 -min 0 -at "double";
	addAttr -ci true -sn "subdivide" -ln "subdivide" -at "long";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 1 0.4627451 0.45882353 ;
	setAttr ".t" -type "double3" 2.3524739139916488 1.3877787807814457e-17 3.5527136788005009e-15 ;
	setAttr ".jo" -type "double3" 1.272221872585407e-14 0 -6.959921409057678 ;
	setAttr ".pa" -type "double3" -3.141027612643135e-15 9.9342689529222003e-14 -3.6219613310495085 ;
	setAttr ".sd" 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "Child";
	setAttr ".mirror" yes;
	setAttr ".wx" -type "double3" 1 0 0 ;
	setAttr ".wy" -type "double3" 0 1 0 ;
	setAttr ".fat" 0.50000000000000011;
	setAttr ".subdivide" 2;
createNode joint -n "Wrist" -p "Elbow";
	rename -uid "17339E7A-4E9F-6840-5F35-38AF61E6AF42";
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
	addAttr -ci true -sn "fat" -ln "fat" -dv 1 -min 0 -at "double";
	addAttr -ci true -sn "subdivide" -ln "subdivide" -at "long";
	addAttr -ci true -sn "n" -ln "name" -dt "string";
	addAttr -ci true -sn "segScaleComp" -ln "segScaleComp" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "fingerShape" -ln "fingerShape" -min 0 -max 5 -en "FK:IK:Spline:Finger:Root:Main" 
		-at "enum";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 1 0.4627451 0.45882353 ;
	setAttr ".t" -type "double3" 2.1682319438539936 1.1102230246251565e-16 -3.5527136788005009e-15 ;
	setAttr ".r" -type "double3" 0 0 -14.999999999999998 ;
	setAttr ".jo" -type "double3" 1.2722218725854067e-14 0 3.6219613310495116 ;
	setAttr ".sd" 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "Hand";
	setAttr ".mirror" yes;
	setAttr ".wx" -type "double3" 1 0 0 ;
	setAttr ".wy" -type "double3" 0 1 0 ;
	setAttr ".fat" 0.50000000000000011;
	setAttr ".n" -type "string" "";
createNode joint -n "WristEnd" -p "Wrist";
	rename -uid "5AF0DBF5-49C6-DACE-E74B-8D97BF0798FE";
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
	addAttr -ci true -sn "fat" -ln "fat" -dv 1 -min 0 -at "double";
	addAttr -ci true -sn "subdivide" -ln "subdivide" -at "long";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 1 1 1 ;
	setAttr ".t" -type "double3" 1.497046947479248 -9.6357220029540908e-16 -3.5527136788005009e-15 ;
	setAttr ".jo" -type "double3" 1.2722218725854067e-14 0 -7.9513867036587919e-16 ;
	setAttr ".sd" 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "End";
	setAttr ".mirror" yes;
	setAttr ".wx" -type "double3" 1 0 0 ;
	setAttr ".wy" -type "double3" 0 1 0 ;
createNode joint -n "WristEnd1" -p "WristEnd";
	rename -uid "7960F236-46FF-C79A-9540-6DA72409926B";
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
	addAttr -ci true -sn "fat" -ln "fat" -dv 1 -min 0 -at "double";
	addAttr -ci true -sn "subdivide" -ln "subdivide" -at "long";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 1 1 1 ;
	setAttr ".t" -type "double3" 0.89075640509356013 -0.84208553695892718 0 ;
	setAttr ".sd" 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "End";
	setAttr ".mirror" yes;
	setAttr ".wx" -type "double3" 1 0 0 ;
	setAttr ".wy" -type "double3" 0 1 0 ;
createNode joint -n "Hip" -p "Root";
	rename -uid "731E93FB-4D9C-BCE5-E004-B885185E31EF";
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
	addAttr -ci true -sn "fat" -ln "fat" -dv 1 -min 0 -at "double";
	addAttr -ci true -sn "subdivide" -ln "subdivide" -at "long";
	addAttr -ci true -sn "n" -ln "name" -dt "string";
	addAttr -ci true -sn "segScaleComp" -ln "segScaleComp" -dv 1 -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "secControl" -ln "secondControl" -dv 1 -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "ikShape" -ln "ikShape" -min 0 -max 5 -en "FK:IK:Spline:Finger:Root:Main" 
		-at "enum";
	addAttr -ci true -sn "fkShape" -ln "fkShape" -min 0 -max 5 -en "FK:IK:Spline:Finger:Root:Main" 
		-at "enum";
	addAttr -ci true -sn "secShape" -ln "secShape" -min 0 -max 2 -en "FKSec:IKSec:SplineSec" 
		-at "enum";
	addAttr -ci true -sn "switchPivot" -ln "switchPivot" -dt "string";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 1 0.4627451 0.45882353 ;
	setAttr ".t" -type "double3" -0.26858851313591003 4.2999868442358932e-16 -1.1393146514892578 ;
	setAttr ".jo" -type "double3" 2.5422485618350694e-16 -2.5681724270185985e-16 -178.84331939540186 ;
	setAttr ".sd" 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "IK";
	setAttr ".mirror" yes;
	setAttr ".wx" -type "double3" 1 0 0 ;
	setAttr ".wy" -type "double3" 0 1 0 ;
	setAttr ".fat" 0.50000000000000011;
	setAttr ".subdivide" 2;
	setAttr ".n" -type "string" "Leg";
	setAttr ".secShape" 1;
	setAttr ".switchPivot" -type "string" "";
createNode transform -n "Leg_Switch_Pivot" -p "Hip";
	rename -uid "1E4F5725-4FCC-01A5-1F9A-F7A90E3AF51F";
	setAttr ".t" -type "double3" 0.97592177128791668 0 -1.471752050392656 ;
	setAttr ".rp" -type "double3" 0 -2.4980018054066022e-16 0 ;
	setAttr ".sp" -type "double3" 0 -2.4980018054066022e-16 0 ;
createNode locator -n "Leg_Switch_PivotShape" -p "Leg_Switch_Pivot";
	rename -uid "7DB4EE7B-4397-DAE4-EA4D-AEACF12DBAEC";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 1 1 0 ;
	setAttr ".lp" -type "double3" 3.3306690738754696e-16 -2.7915031484307728e-16 0 ;
	setAttr ".los" -type "double3" 0.1 0.1 0.1 ;
createNode joint -n "Knee" -p "Hip";
	rename -uid "4BE0A2AC-46E8-0E27-B89C-61842AD50845";
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
	addAttr -ci true -sn "fat" -ln "fat" -dv 1 -min 0 -at "double";
	addAttr -ci true -sn "subdivide" -ln "subdivide" -at "long";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 1 0.4627451 0.45882353 ;
	setAttr ".t" -type "double3" 4.7357963389386599 -5.5511151231257827e-17 -6.6613381477509392e-16 ;
	setAttr ".jo" -type "double3" 2.8701941176451045e-15 3.0666401970734483e-16 -2.5379063475289207 ;
	setAttr ".pa" -type "double3" 1.2567951407226457e-14 1.2874637705292461e-14 -1.3812257429307779 ;
	setAttr ".sd" 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "Child";
	setAttr ".mirror" yes;
	setAttr ".wx" -type "double3" 1 0 0 ;
	setAttr ".wy" -type "double3" 0 1 0 ;
	setAttr ".fat" 0.5;
	setAttr ".subdivide" 2;
createNode joint -n "Ankle" -p "Knee";
	rename -uid "87B804AD-4DA3-5B21-A938-7ABF076202E7";
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
	addAttr -ci true -sn "fat" -ln "fat" -dv 1 -min 0 -at "double";
	addAttr -ci true -sn "subdivide" -ln "subdivide" -at "long";
	addAttr -ci true -sn "n" -ln "name" -dt "string";
	addAttr -ci true -sn "segScaleComp" -ln "segScaleComp" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "heelPivot" -ln "heelPivot" -dt "string";
	addAttr -ci true -sn "footInnerPivot" -ln "footInnerPivot" -dt "string";
	addAttr -ci true -sn "footOuterPivot" -ln "footOuterPivot" -dt "string";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 1 0.4627451 0.45882353 ;
	setAttr ".t" -type "double3" 3.9660151814499267 -3.8857805861880479e-16 -8.8817841970012523e-16 ;
	setAttr ".r" -type "double3" 1.4124500153760508e-30 1.2722218725854067e-14 1.2722218725854067e-14 ;
	setAttr ".jo" -type "double3" -1.4124500153760504e-30 0 1.3812257429307795 ;
	setAttr ".sd" 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "Foot";
	setAttr ".mirror" yes;
	setAttr ".ox" 3;
	setAttr ".wx" -type "double3" 0 -1 0 ;
	setAttr ".oy" 3;
	setAttr ".wy" -type "double3" 0 0 1 ;
	setAttr ".fat" 0.5;
	setAttr ".n" -type "string" "Foot";
	setAttr ".heelPivot" -type "string" "Heel_Pivot";
	setAttr ".footInnerPivot" -type "string" "FootInner_Pivot";
	setAttr ".footOuterPivot" -type "string" "FootOuter_Pivot";
createNode transform -n "Heel_Pivot" -p "Ankle";
	rename -uid "9EF0D60A-43DC-6498-F200-1B8DF613DB05";
	setAttr ".t" -type "double3" 0.84922761464118757 -0.54082792031765015 1.7763568394002505e-15 ;
createNode locator -n "Heel_PivotShape" -p "Heel_Pivot";
	rename -uid "819DA190-4B3F-A01C-B8AD-5DB63F1ABDE0";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 1 1 0 ;
	setAttr ".lp" -type "double3" 1.1102230246251565e-16 0 0 ;
	setAttr ".los" -type "double3" 0.1 0.1 0.1 ;
createNode transform -n "FootOuter_Pivot" -p "Ankle";
	rename -uid "C8CE6DFC-4058-8B7C-08F2-30997656B145";
	setAttr ".t" -type "double3" 0.85122761464118823 1.4452544450759888 -0.46899999999999986 ;
createNode locator -n "FootOuter_PivotShape" -p "FootOuter_Pivot";
	rename -uid "DBB48D77-4495-1D64-8F46-7CA6F3D45AC7";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 1 1 0 ;
	setAttr ".lp" -type "double3" 2.2204460492503131e-16 -2.2204460492503131e-16 0 ;
	setAttr ".los" -type "double3" 0.1 0.1 0.1 ;
createNode transform -n "FootInner_Pivot" -p "Ankle";
	rename -uid "34C735C0-4016-C6BF-55ED-24BFC39F24A8";
	setAttr ".t" -type "double3" 0.85122761464118823 1.4452544450759888 0.46931465148926055 ;
createNode locator -n "FootInner_PivotShape" -p "FootInner_Pivot";
	rename -uid "9A26C57F-4187-01CB-A863-F98BE19696CB";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 1 1 0 ;
	setAttr ".lp" -type "double3" 2.2204460492503131e-16 -2.2204460492503131e-16 0 ;
	setAttr ".los" -type "double3" 0.1 0.1 0.1 ;
createNode joint -n "Toes" -p "Ankle";
	rename -uid "5033B86C-4BE2-FAF4-8796-D08845DA1048";
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
	addAttr -ci true -sn "fat" -ln "fat" -dv 1 -min 0 -at "double";
	addAttr -ci true -sn "subdivide" -ln "subdivide" -at "long";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 1 0.4627451 0.45882353 ;
	setAttr ".t" -type "double3" 0.67734920978546198 1.4452544450759888 -6.6613381477509392e-16 ;
	setAttr ".jo" -type "double3" -0.00055944241997277569 -7.6266146645582075e-05 82.236991315545268 ;
	setAttr ".sd" 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "Child";
	setAttr ".mirror" yes;
	setAttr ".wx" -type "double3" 1 0 0 ;
	setAttr ".wy" -type "double3" 0 1 0 ;
	setAttr ".fat" 0.30000000000000004;
createNode joint -n "ToesEnd" -p "Toes";
	rename -uid "84C307FD-4095-22E4-F5B5-26A4333D3C4D";
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
	addAttr -ci true -sn "fat" -ln "fat" -dv 1 -min 0 -at "double";
	addAttr -ci true -sn "subdivide" -ln "subdivide" -at "long";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 1 1 1 ;
	setAttr ".t" -type "double3" 0.62690100768380508 -3.3306690738754696e-16 0 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".jo" -type "double3" 5.7249922136905293e-14 9.9793370794047899e-20 -3.1805546814635168e-15 ;
	setAttr ".sd" 1;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "End";
	setAttr ".mirror" yes;
	setAttr ".wx" -type "double3" 1 0 0 ;
	setAttr ".wy" -type "double3" 0 1 0 ;
	setAttr ".fat" 0.30000000000000004;
createNode lightLinker -s -n "lightLinker1";
	rename -uid "A049C856-44A8-22F8-A7A2-93A3477456A8";
	setAttr -s 2 ".lnk";
	setAttr -s 2 ".slnk";
createNode shapeEditorManager -n "shapeEditorManager";
	rename -uid "CF9D1EA7-4570-29EA-D0E4-7B87BD4EEBED";
createNode poseInterpolatorManager -n "poseInterpolatorManager";
	rename -uid "46BC7857-4D70-87C4-BD06-629EA4975225";
createNode displayLayerManager -n "layerManager";
	rename -uid "3AB07C53-4598-A098-CB2C-A990BDE24002";
createNode displayLayer -n "defaultLayer";
	rename -uid "36E4C212-4113-094B-8EB7-AC9F9A4FA817";
createNode renderLayerManager -n "renderLayerManager";
	rename -uid "F2D3BE4B-42EC-F131-C954-1FAB9E6B8AAA";
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
		+ "            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1\n            -height 1\n            -sceneRenderFilter 0\n            -activeShadingGraph \"ballora_animatronic_shadow_rig:rsMaterial1SG,ballora_animatronic_shadow_rig:MAT_ballora,ballora_animatronic_shadow_rig:MAT_ballora\" \n            -activeCustomGeometry \"meshShaderball\" \n            -activeCustomLighSet \"defaultAreaLightSet\" \n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Front View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Front View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n"
		+ "        modelEditor -e \n            -docTag \"RADRENDER\" \n            -editorChanged \"updateModelPanelBar\" \n            -camera \"front\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 32768\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n"
		+ "            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -controllers 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n"
		+ "            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1\n            -height 1\n            -sceneRenderFilter 0\n            -activeShadingGraph \"ballora_animatronic_shadow_rig:rsMaterial1SG,ballora_animatronic_shadow_rig:MAT_ballora,ballora_animatronic_shadow_rig:MAT_ballora\" \n            -activeCustomGeometry \"meshShaderball\" \n"
		+ "            -activeCustomLighSet \"defaultAreaLightSet\" \n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Persp View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Persp View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -docTag \"RADRENDER\" \n            -editorChanged \"updateModelPanelBar\" \n            -camera \"persp\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n"
		+ "            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 32768\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n"
		+ "            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -controllers 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n"
		+ "            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 931\n            -height 703\n            -sceneRenderFilter 0\n            -activeShadingGraph \"ballora_animatronic_shadow_rig:rsMaterial1SG,ballora_animatronic_shadow_rig:MAT_ballora,ballora_animatronic_shadow_rig:MAT_ballora\" \n            -activeCustomGeometry \"meshShaderball\" \n            -activeCustomLighSet \"defaultAreaLightSet\" \n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"outlinerPanel\" (localizedPanelLabel(\"\")) `;\n"
		+ "\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\toutlinerPanel -edit -l (localizedPanelLabel(\"\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        outlinerEditor -e \n            -docTag \"isolOutln_fromSeln\" \n            -showShapes 0\n            -showAssignedMaterials 0\n            -showTimeEditor 1\n            -showReferenceNodes 0\n            -showReferenceMembers 0\n            -showAttributes 0\n            -showConnected 0\n            -showAnimCurvesOnly 0\n            -showMuteInfo 0\n            -organizeByLayer 1\n            -organizeByClip 1\n            -showAnimLayerWeight 1\n            -autoExpandLayers 1\n            -autoExpand 0\n            -showDagOnly 1\n            -showAssets 1\n            -showContainedOnly 1\n            -showPublishedAsConnected 0\n            -showParentContainers 0\n            -showContainerContents 1\n            -ignoreDagHierarchy 0\n            -expandConnections 0\n            -showUpstreamCurves 1\n            -showUnitlessCurves 1\n            -showCompounds 1\n"
		+ "            -showLeafs 1\n            -showNumericAttrsOnly 0\n            -highlightActive 1\n            -autoSelectNewObjects 0\n            -doNotSelectNewObjects 0\n            -dropIsParent 1\n            -transmitFilters 0\n            -setFilter \"defaultSetFilter\" \n            -showSetMembers 1\n            -allowMultiSelection 1\n            -alwaysToggleSelect 0\n            -directSelect 0\n            -isSet 0\n            -isSetMember 0\n            -displayMode \"DAG\" \n            -expandObjects 0\n            -setsIgnoreFilters 1\n            -containersIgnoreFilters 0\n            -editAttrName 0\n            -showAttrValues 0\n            -highlightSecondary 0\n            -showUVAttrsOnly 0\n            -showTextureNodesOnly 0\n            -attrAlphaOrder \"default\" \n            -animLayerFilterOptions \"allAffecting\" \n            -sortOrder \"none\" \n            -longNames 0\n            -niceNames 1\n            -selectCommand \"<function selCom at 0x7f29c5c04aa0>\" \n            -showNamespace 1\n            -showPinIcons 0\n"
		+ "            -mapMotionTrails 0\n            -ignoreHiddenAttribute 0\n            -ignoreOutlinerColor 0\n            -renderFilterVisible 0\n            -renderFilterIndex 0\n            -selectionOrder \"chronological\" \n            -expandAttribute 0\n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"outlinerPanel\" (localizedPanelLabel(\"Outliner\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\toutlinerPanel -edit -l (localizedPanelLabel(\"Outliner\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        outlinerEditor -e \n            -docTag \"isolOutln_fromSeln\" \n            -showShapes 0\n            -showAssignedMaterials 0\n            -showTimeEditor 1\n            -showReferenceNodes 0\n            -showReferenceMembers 0\n            -showAttributes 0\n            -showConnected 0\n            -showAnimCurvesOnly 0\n            -showMuteInfo 0\n            -organizeByLayer 1\n            -organizeByClip 1\n"
		+ "            -showAnimLayerWeight 1\n            -autoExpandLayers 1\n            -autoExpand 0\n            -showDagOnly 1\n            -showAssets 1\n            -showContainedOnly 1\n            -showPublishedAsConnected 0\n            -showParentContainers 0\n            -showContainerContents 1\n            -ignoreDagHierarchy 0\n            -expandConnections 0\n            -showUpstreamCurves 1\n            -showUnitlessCurves 1\n            -showCompounds 1\n            -showLeafs 1\n            -showNumericAttrsOnly 0\n            -highlightActive 1\n            -autoSelectNewObjects 0\n            -doNotSelectNewObjects 0\n            -dropIsParent 1\n            -transmitFilters 0\n            -setFilter \"defaultSetFilter\" \n            -showSetMembers 1\n            -allowMultiSelection 1\n            -alwaysToggleSelect 0\n            -directSelect 0\n            -displayMode \"DAG\" \n            -expandObjects 0\n            -setsIgnoreFilters 1\n            -containersIgnoreFilters 0\n            -editAttrName 0\n            -showAttrValues 0\n"
		+ "            -highlightSecondary 0\n            -showUVAttrsOnly 0\n            -showTextureNodesOnly 0\n            -attrAlphaOrder \"default\" \n            -animLayerFilterOptions \"allAffecting\" \n            -sortOrder \"none\" \n            -longNames 0\n            -niceNames 1\n            -showNamespace 1\n            -showPinIcons 0\n            -mapMotionTrails 0\n            -ignoreHiddenAttribute 0\n            -ignoreOutlinerColor 0\n            -renderFilterVisible 0\n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"graphEditor\" (localizedPanelLabel(\"Graph Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Graph Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n                -showShapes 1\n                -showAssignedMaterials 0\n                -showTimeEditor 1\n                -showReferenceNodes 0\n"
		+ "                -showReferenceMembers 0\n                -showAttributes 1\n                -showConnected 1\n                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -organizeByClip 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 1\n                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n                -showParentContainers 1\n                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 1\n                -showCompounds 0\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n                -autoSelectNewObjects 1\n                -doNotSelectNewObjects 0\n                -dropIsParent 1\n                -transmitFilters 1\n                -setFilter \"0\" \n"
		+ "                -showSetMembers 0\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 1\n                -mapMotionTrails 1\n                -ignoreHiddenAttribute 0\n                -ignoreOutlinerColor 0\n                -renderFilterVisible 0\n                $editorName;\n\n\t\t\t$editorName = ($panelName+\"GraphEd\");\n            animCurveEditor -e \n                -displayKeys 1\n                -displayTangents 0\n"
		+ "                -displayActiveKeys 0\n                -displayActiveKeyTangents 1\n                -displayInfinities 0\n                -displayValues 0\n                -autoFit 1\n                -snapTime \"integer\" \n                -snapValue \"none\" \n                -showResults \"off\" \n                -showBufferCurves \"off\" \n                -smoothness \"fine\" \n                -resultSamples 1\n                -resultScreenSamples 0\n                -resultUpdate \"delayed\" \n                -showUpstreamCurves 1\n                -showCurveNames 0\n                -showActiveCurveNames 0\n                -stackedCurves 0\n                -stackedCurvesMin -1\n                -stackedCurvesMax 1\n                -stackedCurvesSpace 0.2\n                -displayNormalized 0\n                -preSelectionHighlight 0\n                -constrainDrag 0\n                -classicMode 1\n                -valueLinesToggle 1\n                -outliner \"graphEditor1OutlineEd\" \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n"
		+ "\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dopeSheetPanel\" (localizedPanelLabel(\"Dope Sheet\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Dope Sheet\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n                -showShapes 1\n                -showAssignedMaterials 0\n                -showTimeEditor 1\n                -showReferenceNodes 0\n                -showReferenceMembers 0\n                -showAttributes 1\n                -showConnected 1\n                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -organizeByClip 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 0\n                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n                -showParentContainers 1\n"
		+ "                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 0\n                -showCompounds 1\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n                -autoSelectNewObjects 0\n                -doNotSelectNewObjects 1\n                -dropIsParent 1\n                -transmitFilters 0\n                -setFilter \"0\" \n                -showSetMembers 0\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n"
		+ "                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 0\n                -mapMotionTrails 1\n                -ignoreHiddenAttribute 0\n                -ignoreOutlinerColor 0\n                -renderFilterVisible 0\n                $editorName;\n\n\t\t\t$editorName = ($panelName+\"DopeSheetEd\");\n            dopeSheetEditor -e \n                -displayKeys 1\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -displayValues 0\n                -autoFit 0\n                -snapTime \"integer\" \n                -snapValue \"none\" \n                -outliner \"dopeSheetPanel1OutlineEd\" \n                -showSummary 1\n                -showScene 0\n                -hierarchyBelow 0\n                -showTicks 1\n                -selectionWindow 0 0 0 0 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n"
		+ "\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"timeEditorPanel\" (localizedPanelLabel(\"Time Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Time Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"clipEditorPanel\" (localizedPanelLabel(\"Trax Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Trax Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = clipEditorNameFromPanel($panelName);\n            clipEditor -e \n                -displayKeys 0\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -displayValues 0\n                -autoFit 0\n                -snapTime \"none\" \n                -snapValue \"none\" \n"
		+ "                -initialized 0\n                -manageSequencer 0 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"sequenceEditorPanel\" (localizedPanelLabel(\"Camera Sequencer\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Camera Sequencer\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = sequenceEditorNameFromPanel($panelName);\n            clipEditor -e \n                -displayKeys 0\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -displayValues 0\n                -autoFit 0\n                -snapTime \"none\" \n                -snapValue \"none\" \n                -initialized 0\n                -manageSequencer 1 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"hyperGraphPanel\" (localizedPanelLabel(\"Hypergraph Hierarchy\")) `;\n"
		+ "\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Hypergraph Hierarchy\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"HyperGraphEd\");\n            hyperGraph -e \n                -graphLayoutStyle \"hierarchicalLayout\" \n                -orientation \"horiz\" \n                -mergeConnections 0\n                -zoom 1\n                -animateTransition 0\n                -showRelationships 1\n                -showShapes 0\n                -showDeformers 0\n                -showExpressions 0\n                -showConstraints 0\n                -showConnectionFromSelected 0\n                -showConnectionToSelected 0\n                -showConstraintLabels 0\n                -showUnderworld 0\n                -showInvisible 0\n                -transitionFrames 1\n                -opaqueContainers 0\n                -freeform 0\n                -imagePosition 0 0 \n                -imageScale 1\n                -imageEnabled 0\n                -graphType \"DAG\" \n"
		+ "                -heatMapDisplay 0\n                -updateSelection 1\n                -updateNodeAdded 1\n                -useDrawOverrideColor 0\n                -limitGraphTraversal -1\n                -range 0 0 \n                -iconSize \"smallIcons\" \n                -showCachedConnections 0\n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"hyperShadePanel\" (localizedPanelLabel(\"Hypershade\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Hypershade\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"visorPanel\" (localizedPanelLabel(\"Visor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Visor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n"
		+ "\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"createNodePanel\" (localizedPanelLabel(\"Create Node\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Create Node\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"polyTexturePlacementPanel\" (localizedPanelLabel(\"UV Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"UV Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"renderWindowPanel\" (localizedPanelLabel(\"Render View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Render View\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"shapePanel\" (localizedPanelLabel(\"Shape Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tshapePanel -edit -l (localizedPanelLabel(\"Shape Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"posePanel\" (localizedPanelLabel(\"Pose Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tposePanel -edit -l (localizedPanelLabel(\"Pose Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dynRelEdPanel\" (localizedPanelLabel(\"Dynamic Relationships\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Dynamic Relationships\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"relationshipPanel\" (localizedPanelLabel(\"Relationship Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Relationship Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"referenceEditorPanel\" (localizedPanelLabel(\"Reference Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Reference Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"componentEditorPanel\" (localizedPanelLabel(\"Component Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Component Editor\")) -mbv $menusOkayInPanels  $panelName;\n"
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
		+ "\t\t\t\t\t\"$panelName = `modelPanel -unParent -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels `;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -docTag \\\"RADRENDER\\\" \\n    -editorChanged \\\"updateModelPanelBar\\\" \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 0\\n    -headsUpDisplay 1\\n    -holdOuts 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 0\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 0\\n    -activeComponentsXray 0\\n    -displayTextures 0\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 32768\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -depthOfFieldPreview 1\\n    -maxConstantTransparency 1\\n    -rendererName \\\"vp2Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -controllers 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -particleInstancers 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -greasePencils 1\\n    -shadows 0\\n    -captureSequenceNumber -1\\n    -width 931\\n    -height 703\\n    -sceneRenderFilter 0\\n    -activeShadingGraph \\\"ballora_animatronic_shadow_rig:rsMaterial1SG,ballora_animatronic_shadow_rig:MAT_ballora,ballora_animatronic_shadow_rig:MAT_ballora\\\" \\n    -activeCustomGeometry \\\"meshShaderball\\\" \\n    -activeCustomLighSet \\\"defaultAreaLightSet\\\" \\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName;\\nmodelEditor -e \\n    -pluginObjects \\\"gpuCacheDisplayFilter\\\" 1 \\n    $editorName\"\n"
		+ "\t\t\t\t\t\"modelPanel -edit -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels  $panelName;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -docTag \\\"RADRENDER\\\" \\n    -editorChanged \\\"updateModelPanelBar\\\" \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 0\\n    -headsUpDisplay 1\\n    -holdOuts 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 0\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 0\\n    -activeComponentsXray 0\\n    -displayTextures 0\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 32768\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -depthOfFieldPreview 1\\n    -maxConstantTransparency 1\\n    -rendererName \\\"vp2Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -controllers 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -particleInstancers 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -greasePencils 1\\n    -shadows 0\\n    -captureSequenceNumber -1\\n    -width 931\\n    -height 703\\n    -sceneRenderFilter 0\\n    -activeShadingGraph \\\"ballora_animatronic_shadow_rig:rsMaterial1SG,ballora_animatronic_shadow_rig:MAT_ballora,ballora_animatronic_shadow_rig:MAT_ballora\\\" \\n    -activeCustomGeometry \\\"meshShaderball\\\" \\n    -activeCustomLighSet \\\"defaultAreaLightSet\\\" \\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName;\\nmodelEditor -e \\n    -pluginObjects \\\"gpuCacheDisplayFilter\\\" 1 \\n    $editorName\"\n"
		+ "\t\t\t\t$configName;\n\n            setNamedPanelLayout (localizedPanelLabel(\"Current Layout\"));\n        }\n\n        panelHistory -e -clear mainPanelHistory;\n        sceneUIReplacement -clear;\n\t}\n\n\ngrid -spacing 5 -size 12 -divisions 5 -displayAxes yes -displayGridLines yes -displayDivisionLines yes -displayPerspectiveLabels no -displayOrthographicLabels no -displayAxesBold yes -perspectiveLabelPosition axis -orthographicLabelPosition edge;\nviewManip -drawCompass 0 -compassAngle 0 -frontParameters \"\" -homeParameters \"\" -selectionLockParameters \"\";\n}\n");
	setAttr ".st" 3;
createNode script -n "sceneConfigurationScriptNode";
	rename -uid "2616AE26-4E0A-1F1F-2A1E-47AFF0543BD5";
	setAttr ".b" -type "string" "playbackOptions -min 1 -max 120 -ast 1 -aet 200 ";
	setAttr ".st" 6;
createNode renderLayerManager -n "curve_file_renderLayerManager";
	rename -uid "30C759DE-4E17-13CF-03F5-F98FD8D1B40C";
createNode renderLayer -n "curve_file_defaultRenderLayer";
	rename -uid "E34E9504-44F8-35F0-D41A-BB87471D19C5";
	setAttr ".g" yes;
createNode nodeGraphEditorInfo -n "MayaNodeEditorSavedTabsInfo";
	rename -uid "F7E4C657-4370-D6CF-03F7-A1AAFE71D84F";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" 820.60939923409546 -1701.6123065629597 ;
	setAttr ".tgi[0].vh" -type "double2" 1954.7879960368352 -1149.2313761316541 ;
createNode objectSet -n "AllSet";
	rename -uid "038C5DD0-4834-F435-0B2E-E9920F7897F5";
	setAttr ".ihi" 0;
createNode objectSet -n "Sets";
	rename -uid "9FF674D9-4865-D363-A815-A98ECFB9D996";
	setAttr ".ihi" 0;
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
	setAttr -s 2 ".r";
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
connectAttr "WristEnd.s" "WristEnd1.is";
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
connectAttr "curve_file_renderLayerManager.rlmi[0]" "curve_file_defaultRenderLayer.rlid"
		;
connectAttr "AllSet.msg" "Sets.dnsm" -na;
connectAttr "defaultRenderLayer.msg" ":defaultRenderingList1.r" -na;
connectAttr "curve_file_defaultRenderLayer.msg" ":defaultRenderingList1.r" -na;
// End of my3.ma
