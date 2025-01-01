from django import forms


class BeforeDeliveryForm(forms.Form):
    # Врастание плаценты (1 или 0)
    placenta_previa = forms.ChoiceField(
        label='Врастание плаценты',
        choices=[(1, 'Да'), (0, 'Нет')],
        widget=forms.RadioSelect,
        required=True
    )

    # Предлежание плаценты (1 или 0)
    indications_for_caesarean_1 = forms.ChoiceField(
        label='Предлежание плаценты',
        choices=[(1, 'Да'), (0, 'Нет')],
        widget=forms.RadioSelect,
        required=True
    )

    # Задняя стенка (1 или 0)
    placenta_localization_3 = forms.ChoiceField(
        label='Локализация плаценты по задней стенке',
        choices=[(1, 'Да'), (0, 'Нет')],
        widget=forms.RadioSelect,
        required=True
    )

    # Кесарево сечение (1 или 0)
    delivery_2_0 = forms.ChoiceField(
        label='Кесарево сечение',
        choices=[(1, 'Да'), (0, 'Нет')],
        widget=forms.RadioSelect,
        required=True
    )

    # Возраст (лет)
    age = forms.IntegerField(label='Возраст, лет', min_value=0, required=True)

    # Срок беременности (недели)
    gestational_age = forms.FloatField(label='Срок беременности, недели', min_value=0, required=True)

    # Фибриноген (г/л)
    fibrinogen = forms.FloatField(label='Фибриноген, г/л', min_value=0, required=True)


class AtDeliveryForm(forms.Form):
    # АД систолическое, мм.рт.ст.
    bp_systolic = forms.IntegerField(label='АД систолическое, мм.рт.ст.', min_value=0, required=True)

    # Частота сердечных сокращений, в мин.
    heart_rate = forms.IntegerField(label='Частота сердечных сокращений, в мин.', min_value=0, required=True)

    # Гемоглобин, г/л
    hemoglobin = forms.FloatField(label='Гемоглобин, г/л', min_value=0, required=True)

    # Гематокрит, %
    hematocrit = forms.FloatField(label='Гематокрит, %', min_value=0, required=True)

    # Тромбоциты, 10^9/ л
    thrombocytes = forms.IntegerField(label='Тромбоциты, 10^9/ л', min_value=0, required=True)

    # Протромбиновый индекс (ПТИ), %
    prothrombin_index = forms.FloatField(label='Протромбиновый индекс (ПТИ), %', min_value=0, required=True)
