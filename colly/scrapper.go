package main

import (
	"fmt"
	"github.com/gocolly/colly/v2"
	"strings"
)

type Item struct {
	IdLaptop    string `json:"idLaptop"`
	Name        string `json:"name"`
	Description string `json:"description"`
	Stars       string `json:"stars"`
	Reviews     string `json:"reviews"`
}

func laptopsLinkGenerator(brand string) []string {
	brand = strings.ToUpper(brand)
	baseurl := "https://webscraper.io"
	var linksList []string

	collector := colly.NewCollector()

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
