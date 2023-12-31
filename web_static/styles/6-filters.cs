.filters {
    background-color: white;
    height: 70px;
    width: 100%;
    border: 1px solid;
    border-color: #DDDDDD;
    border-radius: 4px;
    justify-content: flex-end;
    display: flex;
    align-items: center;
    

}
section.filters button {
    font-size: 18px;
    background-color: #ff5a5f;
    color: #ffffff;
    height: 48px;
    width: 30%;
    border: 0;
    text-align: center;
    border-radius: 4px;
    margin-right: 30px;
    opacity: 1;
}

section.filters button:hover {
    opacity: 0.9;
}
.locations, .amenities {
    height: 100%;
    width: 25%;
    display: block;
    position: relative;
    padding-right:30%;
}
.locations {
    border-right: #DDDDDD 1px solid;

}
.locations h3, .amenities h3{
    font-weight: 600;
    margin: 19.5px 55px -20px 40px;
}
.locations h4, .amenities h4{
    font-weight: 400;
    font-size: 14px;
    margin: 20px 0px 0px 40px;
}
div.container section.filters .popover{
    background-color: #fafafa;
    width: 25%;
    border-color: #DDDDDD;
    border: 1px solid;
    position: absolute;
    border-radius: 4px;
   list-style-type: none;
   visibility: hidden;
}

div.container section.filters ul.popover li.h2 {
    font-size: 16px;
}
div.container section.filters ul.popover li {
    list-style-type: none;
}
div.container section.filters .locations:hover .popover,
div.container section.filters .amenities:hover .popover{
    visibility: visible;
}
