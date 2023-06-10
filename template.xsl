<?xml version="1.0" encoding="UTF-8" ?>
<xsl:transform xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="2.0">
    <xsl:output method="html" encoding="UTF-8" indent="no" />
    
    <xsl:template match="/">
          <xsl:apply-templates select="data/object"/>
    </xsl:template>
      
    <xsl:template match="*">
      <xsl:value-of select="emoji"/>&#xA0;&#xA0;<a href="{link}"><xsl:value-of select="text"/>...</a><br />
          <xsl:value-of select="channel"/><br /><br />
          <xsl:text>&#xa;</xsl:text>
    </xsl:template>    
</xsl:transform>
