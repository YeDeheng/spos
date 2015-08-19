from HTMLParser import HTMLParser

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        #return self.fed
        return ' '.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

# test
#html = '<p>I am wondering about any "best practices" to integrate a "modern JavaScript build workflow" into a Maven build that produces a WAR artifact.</p>&#xA;&#xA;<p>I have found several maven plugins that handle concatenation and minification:</p>&#xA;&#xA;<ul>&#xA;<li>WRO4J: <a href="https://code.google.com/p/wro4j/wiki/MavenPlugin" rel="nofollow">https://code.google.com/p/wro4j/wiki/MavenPlugin</a></li>&#xA;<li>Minify Maven Plugin: <a href="https://github.com/samaxes/minify-maven-plugin" rel="nofollow">https://github.com/samaxes/minify-maven-plugin</a></li>&#xA;<li>YUI: <a href="http://alchim.sourceforge.net/yuicompressor-maven-plugin/" rel="nofollow">http://alchim.sourceforge.net/yuicompressor-maven-plugin/</a></li>&#xA;</ul>&#xA;&#xA;<p>However I am still missing how they fit into a full build workflow, since I think it is mandatory to be able to switch concatenation/minification on and off:</p>&#xA;&#xA;<p>For development I want to build a WAR that does not contain the concatenated/minified resources so that I can conveniently debug. For a production build I want to produce a WAR that contains the concatenated/minified resources.</p>&#xA;&#xA;<p>Additionally for the production build I then have to "rewrite" the script URLs in my html to point to the concatenate/minified version(s) of the script(s).</p>&#xA;&#xA;<p>In the JavaScript world I would use Grunt with different grunt tasks (uglify, usemin) to achieve the above workflow. How can I achieve the same in a Maven build?</p>&#xA;'
#print strip_tags(html)