
from ExioVisuals.models import Product, Selection, Selection2, Selection3, Country, Substance
from django import forms
from IEMasterProject.widgets import FancyTreeWidget
from ExioVisuals.models import years
class modes(forms.Form):
    CHOICES=[('selectA','Consumed product category'),('selectB','Consuming region'),
          ('selectC','Sector where impact occurs')   ,('selectD','Country where impact occurs')
    ,('selectE','Environmental pressure [not functional yet]')
    ,('selectF','Year')

    ]

    y = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())

    def __init__(self, *args, **kwargs):
        super(modes, self).__init__(*args, **kwargs)
        self.fields['y'].label = ":"
class yearsSingleSelect(forms.Form):

    p = []
    t = []
    absData = years.objects.all().values_list('years', flat=True)
    for x in absData:
        p.append(x+"#"+x)
    for x in p:
         t.append(x.split('#'))
    print(t)
    k = t

    Year = forms.ChoiceField(
                                         choices=k)
    def __init__(self, *args, **kwargs):
        super(yearsSingleSelect, self).__init__(*args, **kwargs)
        self.fields['Year'].label = ""

class yearsMultipleSelect(forms.Form):

    p = []
    t = []
    absData = years.objects.all().values_list('years', flat=True)
    for x in absData:
        p.append(x+"#"+x)
    for x in p:
         t.append(x.split('#'))
    print(t)
    OPTIONS = t

    Year = forms.MultipleChoiceField(widget=forms.SelectMultiple(attrs={'size':'10,10'}),
                                             choices=OPTIONS)
class PostFormEFactor(forms.Form):
    name = forms.CharField()
    grams = forms.FloatField()
    OPTIONS = (
            ("a", "Achoice"),
            ("b", "Bchoice"),
            )
    names = forms.MultipleChoiceField(
                                         choices=OPTIONS)
    OPTIONS2 = (
            ("a", "Achoice"),
            ("b", "Bchoice"),
            )
    names2 = forms.ChoiceField(
                                         choices=OPTIONS2)



    CHOICES=[('select1','select 1'),('select2','select 2')]

    like = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())

class reloadForm(forms.Form):
    CHOICES=[('select1','mode 1'),('select2','mode 2')]

    selection = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())

products = Product.objects.order_by('tree_id', 'lft')
countries = Country.objects.order_by('tree_id', 'lft')
substances = Substance.objects.order_by('tree_id', 'lft')

class ProductSelectionForm(forms.ModelForm):
    class Meta:
        model = Selection
        fields = ( 'products',)
        widgets = {
            'products': FancyTreeWidget(queryset=products)
        }

class CountrySelectionForm(forms.ModelForm):
    class Meta:
        model = Selection2
        fields = ( 'countries',)
        widgets = {
            'countries': FancyTreeWidget(queryset=countries)
        }

class SubstanceSelectionForm(forms.ModelForm):
    class Meta:
        model = Selection3
        fields = ( 'substances',)
        widgets = {
            'substances': FancyTreeWidget(queryset=substances)
        }