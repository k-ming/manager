# yunshen
云绅测试脚本

## selenium的css定位
#### 一、定位遇到的问题:
    1、Element is visible 使用xpath定位，其中用@class属性来定位，也会报这个错误（特别是class中含有复合类的定位）
    2、用selenium做自动化，有时候会遇到需要模拟鼠标操作才能进行的情况，比如单击、双击、点击鼠标右键、拖拽等等。而selenium给我们提供了一个类来处理这类事件——ActionChains
#### 二、xpath、css定位比较
##### 1、css选择器匹配规则
|选择器|示例|描述|支持的css版本|
| --- |:--:|:-- |:--|
|.class|.info|选择class="info"的所有元素|1|
|#id|#firstname|选择id="firstname"的所有元素|1|
|* |*|选择所有元素|2|
|element|p|选择所有<p>元素|1|
|element,element|div,p|选择所有\<div>元素和所有\<p>元素|1|
|element element|div p|选择\<div>元素内部的所有\<p>元素|1|
|element>element|div>p|选择父元素为\<div>的所有子元素\<p>元素|2|
|element+element|div+p|选择紧接在\<div>元素之后的所有\<p>元素|2|
|[attribute]|[target]|选择带有target属性的所有元素|2|
|[attribute=vulue]|[target=_blank]|选择target="_blank"的所有元素|2|
|[attribute~=vulue]|title~=flower|选择title属性包含"flower"的所有元素|2|
|[attribute|=vulue]|[lang\|=en]|选择lang属性值以"en"开头的所有元素|2|
|:link| a:link|选择所有未被访问的链接|1|
|:visited| a:visited|选择所有已被访问的链接|1|
|:active| a:active|选择活动链接|1|
|:hover| a:hover|选择鼠标位于其上的链接|1|
|:focus| input:focus|选择获得焦点的input元素|2|
|:first-letter| P:first-letter|选择每个\<p>元素的首字母|1|
|:first-child| p:first-child|选择属于父元素的第一个子元素的每个\<p>元素|2|
|:first-line| P:first-line| 选择每个\<p>元素的首行|1|
|:before| p:before|在每个\<p>元素的内容之前插入内容|2|
|p:after| p:after|在每个\<p>元素的内容之后插入内容|2|
|:lang(language)| p:lang(it)|选择带有以"it"开头的lang属性的每个\<p>元素|2|
|element1~element2| p~ul|选择前面有\<p>元素的每个\<ul>|3|
|[attribute^=value]| a[src^="https"]| 选择其src属性值以"https"开头的每个\<a>元素|3|
|[attrubute$=value]| a[src$=".pdf"]| 选择其src属性以".pdf"结尾的所有\<a>元素|3|
|[attrubute*=value]| a[src*="abc"]|选择其src属性包含"adc"字符串的所有\<a>元素|3|
|:first-of-type| p:first-of-type|选择属于其父元素的首个\<p>的每个\<p>元素|3|
|:last-of-type| p:last-of-type|选择属于其父元素的最后一个\<p>的每个\<p>元素|3|
|:only-of-type| p::only-of-type|选择属于其父元素唯一的\<p>的每个\<p>元素|3|
|:only-child| p::only-child|选择属于其父元素唯一子元素的\<p>元素|3|
|:nth-child(n)| p::nth-child(2)|选择属于其父元素第二子元素的\<p>元素|3|
|:nth-last-child(n)| P:nth-last-child(2)|选择属于其父元素倒数第二子元素的\<p>元素|3|
|:nth-of-type(n)| p:nth-of-type(2)|选择属于其父元素第二个\<p>的每个\<p>|3|
|:nth-last-of-type(n)| p:nth-last-of-type(2)|选择属于其父元素倒数第二个\<p>的每个\<p>|3|
|:last-child| P:last-child|选择属于其父元素最后一个子元素每个\<p>元素|3|
|:root| :root| 选择文档的根元素|3|
|:empty| p:empty|选择没有子元素的\<p>元素（包括文本节点）|3|
|:target| #news:target|选择当前活动的#news元素|3|
|:enabled| input:enabled|选择每个启动\<input>元素|3|
|:disabled| input:disabled| 选择每禁用的\<input>元素|3|
|:checked| input:checked| 选择每个被选中的\<input>元素|3|
|:not(selector)| :not(p)|选择非\<p>元素的每个元素|3|
|::selection| ::selection|选择被用户选取的元素部分|3|

#### 2、定位实例，以如下html文档为例
```html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
 <head>
  <title> css locate </title>
 </head>
 <body>
  <div class="formdiv">
    <form name="fnfn">
        <input name="username" type="text"></input>
        <input name="password" type="text"></input>
        <input name="continue" type="button"></input>
        <input name="cancel" type="button"></input>
        <input value="SYS123456" name="vid" type="text">
        <input value="ks10cf6d6" name="cid" type="text">
    </form>
    <div class="subdiv">
        <a href="http://www.baidu.com" id="baiduUrl">baidu</a>
        <ul id="recordlist">
            <p>Heading</p>
            <li>Cat</li>
            <li>Dog</li>
            <li>Car</li>
            <li>Goat</li>
        </ul>
    </div>
  </div>
 </body>
</html>
```
#### 3、css选择定位实例
|cssSelector|	匹配|
|---|:---|
|css=div|\<div class="formdiv">|
|css=div.formdiv|	\<div class="formdiv">|
|css=#recordlist <br>  css=ul#recordlist| \<ul id="recordlist">|
|css=div.subdiv p|	\<p>Heading\</p>|
|css=div.subdiv>ul>p|	\<p>Heading\</p>|
|css=form+div|	\<div class="subdiv">|
|css=p+li|	\<li>Cat\</li> |
|css=p~li|	\<li>Cat\</li> 得到4个li中的第一个|
|css=form>input[name=username]|\<input name="username" type="text"></input>|
|css=input[name$=id][value^=SYS]|	\<input value="SYS123456" name="vid" type="text">|
|css=input[value*='SYS']|	\<input value="SYS123456" name="vid" type="text">|
|css=a:link|	\<a href="http://www.baidu.com">baidu\</a>|
|css=input:first-child|	\<input name="username" type="text"></input>|
|css=input:last-child|	\<input value="ks10cf6d6" name="cid" type="text">|
|css=li:nth-child(2)|	\<li>Cat\</li> 因为这个li是ul下的第二个元素，所以是child（2）|
|css=:root|	\<html>|

#### 4、XPATH和CSS定位比较，以上面的html为例
|定位方式|	XPath|	CSS|
|---|:--:|:--:|
|标签|	//div|	div|
|By id|	//div[@id='recordlist']	|div#recordlist|
|By class|	//div[@class='subdiv'] <br> //div[contains(@class,'subdiv')]|	div.subdiv
|By 属性|	//input[@name='username']|	input[name=username] <br> input[name^=user] <br> input[name$=name] <br> input[name*=erna]<br>|
|定位子元素|	//ul[@id='recordlist']/* <br> //ul/p|ul#recordlist>* <br> ul#recordlist>p|
|定位后代元素|	//div[@class='subdiv']//p|	div p|
|By index|	//li[4] 定位第四个li|	li:nth-child(5)|
|By content|	//li[contains(text(),'Goa')]|	li contains('Goa') 该方法已经废弃|
|根据子元素回溯定位父元素|//*[./a[@id='baiduUrl']] <br> //div[.//p[text()='Heading']] <br> 匹配到：\<div class="subdiv">|	？|
|根据兄弟元素定位|	//ul[preceding-sibling::a[@id='baiduUrl']]<br>//ul[preceding-sibling::a[//div[@class='subdiv']/a]]<br>都匹配到：\<ul id="recordlist">|	a+ul<br>a#baiduUrl+ul<br>匹配到：\<ul id="recordlist">|

`注意：根据兄弟元素定位时只能从上面的兄弟找下面的兄弟，如：css=p+li，写成li+p是不行的。`<br>
`可以看到，CSS定位语法比XPath更为简洁、灵活，而且CSS定位的速度还比XPath快，推荐使用CSS定位.`
