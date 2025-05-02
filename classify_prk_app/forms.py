from django import forms


class WlabForm(forms.Form):
    # Число предшествующих родов (от 0 до 7)
    number_deliveries = forms.IntegerField(label='Паритет родов, случаи', min_value=0, max_value=7, required=True)

    # Гемоглобин (от 42 до 143)
    hemoglobin = forms.IntegerField(label='Гемоглобин, г/л', min_value=42, max_value=143, required=True)

    # Гематокрит (от 12.6 до 42.6)
    hematocrit = forms.FloatField(label='Гематокрит, %', min_value=12.6, max_value=42.6, required=True)

    # Активированное частичное тромбопластиновое время (АЧТВ) (от 18 до 58)
    aptt = forms.IntegerField(label='АЧТВ, сек.', min_value=18, max_value=58, required=True)

    # Фибриноген (г/л) (от 2.2 до 8)
    fibrinogen = forms.FloatField(label='Фибриноген, г/л', min_value=2.2, max_value=8, required=True)


class WolabForm(forms.Form):
    # Возраст пациентки, мм.рт.ст. (от 15 до 48)
    age = forms.IntegerField(label='Возраст, лет', min_value=15, max_value=48, required=True)

    # Наличие кесарева сечения в анамнезе (1, 0)
    cesarean_history = forms.ChoiceField(
        label='Наличие кесарева\nсечения в анамнезе',
        choices=[(1, 'Да'), (0, 'Нет')],
        widget=forms.RadioSelect,
        required=True
    )

    # Возраст менархе (от 10 до 18)
    menarche = forms.IntegerField(label='Возраст менархе, лет', min_value=10, max_value=18, required=True)

    # Передняя стенка (1, 0)
    placenta_localization___2 = forms.ChoiceField(
        label='Плацента на передней\nстенке матки',
        choices=[(1, 'Да'), (0, 'Нет')],
        widget=forms.RadioSelect,
        required=True
    )

    # Кесарево сечение экстренная операция (1, 0)
    caesarean_section_1_0 = forms.ChoiceField(
        label='Экстренное кесарево\nсечение',
        choices=[(1, 'Да'), (0, 'Нет')],
        widget=forms.RadioSelect,
        required=True
    )
