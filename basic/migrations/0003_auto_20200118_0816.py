# Generated by Django 2.2.9 on 2020-01-18 08:16

from django.db import migrations
import streams.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0002_basicpage_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicpage',
            name='body',
            field=wagtail.core.fields.StreamField([('cta', wagtail.core.blocks.StructBlock([('text_alignment', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Left'), ('right', 'Right')])), ('content', wagtail.core.blocks.RichTextBlock(features=['h3', 'link', 'bold', 'italic'])), ('image', wagtail.images.blocks.ImageChooserBlock()), ('link', wagtail.core.blocks.StructBlock([('link_text', wagtail.core.blocks.CharBlock(default='Read More', max_length=50)), ('internal_link', wagtail.core.blocks.PageChooserBlock(help_text='Select an internal page to link to. Internal links are used before external links (if both are provided).', required=False)), ('external_link', wagtail.core.blocks.URLBlock(help_text='Type an external website to link to. Internal links are used before external links (if both are provided).', required=False))]))])), ('large_text', streams.blocks.LargeTextBlock()), ('large_listing_block', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('text_alignment', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Left'), ('right', 'Right')])), ('title', wagtail.core.blocks.CharBlock(max_length=50)), ('internal_link', wagtail.core.blocks.PageChooserBlock(help_text='Select an internal page to link to. Internal links are used before external links (if both are provided).', required=False)), ('external_link', wagtail.core.blocks.URLBlock(help_text='Type an external website to link to. Internal links are used before external links (if both are provided).', required=False))])), ('small_listing_block', wagtail.core.blocks.StructBlock([('cards', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('year', wagtail.core.blocks.CharBlock(help_text='Optional. Small text at the top of the card.', max_length=20, required=False)), ('title', wagtail.core.blocks.CharBlock(max_length=50)), ('internal_link', wagtail.core.blocks.PageChooserBlock(help_text='Select an internal page to link to. Internal links are used before external links (if both are provided).', required=False)), ('external_link', wagtail.core.blocks.URLBlock(help_text='Type an external website to link to. Internal links are used before external links (if both are provided).', required=False))])))])), ('richtext', wagtail.core.blocks.RichTextBlock(features=['h3', 'bold', 'italic', 'ol', 'ul', 'link'], group='Text Sections', template='streams/simple_richtext_block.html')), ('buttons', wagtail.core.blocks.StructBlock([('buttons', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('link_text', wagtail.core.blocks.CharBlock(default='Read More', max_length=50)), ('internal_link', wagtail.core.blocks.PageChooserBlock(help_text='Select an internal page to link to. Internal links are used before external links (if both are provided).', required=False)), ('external_link', wagtail.core.blocks.URLBlock(help_text='Type an external website to link to. Internal links are used before external links (if both are provided).', required=False))])))])), ('two_thirds', wagtail.core.blocks.StructBlock([('large_image_alignment', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Left'), ('right', 'Right')])), ('two_thirds_image', wagtail.images.blocks.ImageChooserBlock()), ('one_third_image', wagtail.images.blocks.ImageChooserBlock())])), ('two_thirds_text', wagtail.core.blocks.StructBlock([('text_alignment', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Left'), ('right', 'Right')])), ('image', wagtail.images.blocks.ImageChooserBlock()), ('content', wagtail.core.blocks.RichTextBlock(features=['h3', 'link', 'bold', 'italic'])), ('link', wagtail.core.blocks.StructBlock([('link_text', wagtail.core.blocks.CharBlock(default='Read More', max_length=50)), ('internal_link', wagtail.core.blocks.PageChooserBlock(help_text='Select an internal page to link to. Internal links are used before external links (if both are provided).', required=False)), ('external_link', wagtail.core.blocks.URLBlock(help_text='Type an external website to link to. Internal links are used before external links (if both are provided).', required=False))]))])), ('image_row', wagtail.core.blocks.StructBlock([('image_rows', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('row', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock())], icon='image')))])))])), ('hr', streams.blocks.HorizontalRuleBlock()), ('two_images_and_text', wagtail.core.blocks.StructBlock([('text_alignment', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Left'), ('right', 'Right')])), ('one_third_image', wagtail.images.blocks.ImageChooserBlock()), ('one_third_image_2', wagtail.images.blocks.ImageChooserBlock()), ('content', wagtail.core.blocks.RichTextBlock(features=['h3', 'link', 'bold', 'italic'])), ('link', wagtail.core.blocks.StructBlock([('link_text', wagtail.core.blocks.CharBlock(default='Read More', max_length=50)), ('internal_link', wagtail.core.blocks.PageChooserBlock(help_text='Select an internal page to link to. Internal links are used before external links (if both are provided).', required=False)), ('external_link', wagtail.core.blocks.URLBlock(help_text='Type an external website to link to. Internal links are used before external links (if both are provided).', required=False))]))])), ('two_column', wagtail.core.blocks.StructBlock([('large_image_alignment', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Left'), ('right', 'Right')])), ('small_image', wagtail.images.blocks.ImageChooserBlock()), ('small_image_2', wagtail.images.blocks.ImageChooserBlock()), ('large_image', wagtail.images.blocks.ImageChooserBlock())]))], blank=True, null=True),
        ),
    ]
