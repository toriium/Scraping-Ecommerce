package main

import (
	"fmt"
	"github.com/gocolly/colly/v2"
	"strings"
)

type Item struct {
	IdLaptop    string `json:"IdLaptop"`
	Name        string `json:"Name"`
	Description string `json:"Description"`
	Stars       string `json:"Stars"`
	Reviews     string `json:"Reviews"`
	Price       string `json:"Price"`
}

func laptopsLinkGenerator(brand string) []string {
	brand = strings.ToUpper(brand)
	baseurl := "https://webscraper.io"
	var linksList []string

	ua := "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
	collector := colly.NewCollector(colly.UserAgent(ua))

	collector.OnHTML(`div[class="caption"] > h4:nth-child(2) > a`, func(e *colly.HTMLElement) {

		title := strings.ToUpper(e.Attr("title"))
		if strings.Contains(title, brand) {
			href := e.Attr("href")
			linksList = append(linksList, baseurl+href)
		}
	})

	collector.Visit("https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops")

	return linksList
}
func crawler(brand string) []Item {
	laptopLinks := laptopsLinkGenerator(brand)

	var laptopsList []Item
	collector := colly.NewCollector()
	for _, link := range laptopLinks {

		collector.OnHTML("body", func(element *colly.HTMLElement) {
			var stars int
			element.ForEach(`div[class="ratings"]>p>span`, func(i int, element *colly.HTMLElement) { stars++ })

			item := Item{
				IdLaptop:    link,
				Name:        element.ChildText("h4:nth-child(2)"),
				Description: element.ChildText(`[class="description"]`),
				Stars:       string(rune(stars)),
				Reviews:     element.ChildText(`div[class="ratings"]>p`),
				Price:       element.ChildText(`[class="pull-right price"]`),
			}

			laptopsList = append(laptopsList, item)

		})

		collector.Visit(link)

	}
	return laptopsList
}

func main() {
	result := crawler("lenovo")
	for _, v := range result {
		fmt.Printf("%+v\n", v)
	}

}
