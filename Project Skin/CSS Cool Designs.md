![[Pasted image 20231203090944.png]]
```css
.reel{
	--gap: Irem;
	display: grid;
	gap: var(--gap);
	grid-auto-flow: column;
	grid-auto-columns: 30%;
	overflow-x: scroll;
	scroll-snap-type: x mandatory;
	scroll-padding: var(--gap);
}
.reel > * {
	scroll-snap-align: start;
}
```