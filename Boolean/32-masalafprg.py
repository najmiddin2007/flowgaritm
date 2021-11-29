<?xml version="1.0"?>
<flowgorithm fileversion="2.11">
    <attributes>
        <attribute name="name" value=""/>
        <attribute name="authors" value="3D"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2021-10-03 02:41:01 "/>
        <attribute name="created" value="M0Q7SjdSRlNDNjsyMDIxLTEwLTAzOyIwMjozOToxMSAiOzE3ODQ="/>
        <attribute name="edited" value="M0Q7SjdSRlNDNjsyMDIxLTEwLTAzOyIwMjo0MTowMSAiOzE7MTg4NA=="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="a, b, c" type="Integer" array="False" size=""/>
            <declare name="d" type="Boolean" array="False" size=""/>
            <input variable="a"/>
            <input variable="b"/>
            <input variable="c"/>
            <assign variable="d" expression="a==b or b==c or a==c"/>
            <output expression="d" newline="True"/>
        </body>
    </function>
</flowgorithm>
