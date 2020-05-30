import { Directive, Renderer2, HostListener, ElementRef} from '@angular/core';

@Directive({
  selector: '[appHighlight]'
})

/**
 * Directive for highlighting a menu item
 */
export class HighlightDirective {

  constructor(
    private el: ElementRef,
    private renderer: Renderer2
  ) { }

  /**
   * Highlight on mouse enter
   * @param 'mouseenter' 
   */
  @HostListener('mouseenter') onmouseenter() {
    this.renderer.addClass(this.el.nativeElement, 'highlight')
  }

  /**
   * Highlight on mouse leave
   * @param 'mouseleave' 
   */
  @HostListener('mouseleave') onmouseleave() {
    this.renderer.removeClass(this.el.nativeElement, 'highlight')
  }

}
