<?xml version="1.0" encoding="UTF-8" ?>
<xsl:transform xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="2.0">
    <xsl:output method="html" encoding="UTF-8" indent = "no"/>
    
    <xsl:template match="/">
          <xsl:apply-templates select="data/object"/>
    </xsl:template>
      
    <xsl:template match="*">
     <xsl:value-of select="emoji"/> <xsl:value-of select="channel"/> 🔗 <a href="{link}"><xsl:value-of select="text" /></a>
          <xsl:text>&#xa;</xsl:text>
          <xsl:text>&#xa;</xsl:text>
    </xsl:template>    
</xsl:transform>
