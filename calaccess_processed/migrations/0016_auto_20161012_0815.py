# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-12 08:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calaccess_processed', '0015_auto_20160928_0458'),
    ]

    operations = [
        migrations.CreateModel(
            name='CandidateCommittee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidate_filer_id', models.IntegerField(help_text='Unique filer_id of the candidate. Derived from FILER_ID_A and FILER_ID_B columns on FILER_LINKS_CD, includes any filer_id ever categorized as a candidate in FILER_TO_FILER_TYPES_CD.', verbose_name='candidate filer ID')),
                ('committee_filer_id', models.IntegerField(help_text='Unique filer_id of the committee linked to the candidate. Derived from FILER_ID_A and FILER_ID_B columns on FILER_LINKS_CD, includes any filer_id ever categorized as a recipient committee that is linked to a filer_id categorized as a candidate in FILER_TO_FILER_TYPES_CD.', verbose_name='committee filer ID')),
                ('link_type_id', models.IntegerField(help_text='Numeric identifier that describes how the candidate and committee are linked (the absolute value of FILER_LINKS_CD.LINK_TYPE).', verbose_name='link type identifier')),
                ('link_type_description', models.CharField(help_text='Human-readable description of the link between the candidate and committee (from LOOKUP_CODES_CD.CODE_DESC).', max_length=100, verbose_name='link type description')),
                ('first_session', models.IntegerField(help_text='First session when the link between the candidate and commitee existed (minimum value of FILER_LINKS_CD.SESSION_ID).', null=True, verbose_name='first session')),
                ('last_session', models.IntegerField(help_text='Last session when the link between the candidate and commitee existed (maximum value of FILER_LINKS_CD.SESSION_ID).', null=True, verbose_name='last session')),
                ('first_effective_date', models.DateField(help_text='Earliest date when the link between the candidate and commitee was in effect (minimum value of FILER_LINKS_CD.EFFECTIVE_DATE).', verbose_name='first effective date')),
                ('last_effective_date', models.DateField(help_text='Latest date when the link between the candidate and commitee was in effect (maximum value of FILER_LINKS_CD.EFFECTIVE_DATE).', verbose_name='last effective date')),
                ('first_termination_date', models.DateField(help_text='Earliest date when the link between the candidate and commitee was terminated (minimum value of FILER_LINKS_CD.TERMINATION_DATE).', null=True, verbose_name='first termination date')),
                ('last_termination_date', models.DateField(help_text='Latest date when the link between the candidate and commitee was terminated (minimum value of FILER_LINKS_CD.TERMINATION_DATE).', null=True, verbose_name='last termination date')),
            ],
        ),
        migrations.CreateModel(
            name='F460Filing',
            fields=[
                ('date_filed', models.DateField(db_index=True, help_text='Date this report was filed, according to the filer (from CVR_CAMPAIGN_DISCLOSURE.RPT_DATE)', verbose_name='date filed')),
                ('from_date', models.DateField(db_index=True, help_text='The first date of the filing period covered by the statement (from CVR_CAMPAIGN_DISCLOSURE.FROM_DATE)', verbose_name='from date')),
                ('thru_date', models.DateField(db_index=True, help_text='The last date of the filing period covered by the statement (from CVR_CAMPAIGN_DISCLOSURE.THRU_DATE)', verbose_name='thru date')),
                ('filer_id', models.IntegerField(db_index=True, help_text='Numeric filer identification number (from FILER_XREF.FILER_ID)', verbose_name='filer id')),
                ('filer_lastname', models.CharField(help_text='Last name of filer (from CVR_CAMPAIGN_DISCLOSURE.FILER_NAML)', max_length=200, verbose_name='filer last name')),
                ('filer_firstname', models.CharField(blank=True, help_text='First name of the filer (from CVR_CAMPAIGN_DISCLOSURE.FILER_NAMF)', max_length=45, verbose_name='filer first name')),
                ('election_date', models.DateField(db_index=True, help_text='Date of the election in which the filer is participating (from CVR_CAMPAIGN_DISCLOSURE.ELECT_DATE)', null=True, verbose_name='election date')),
                ('monetary_contributions', models.IntegerField(help_text='Total monetary contributions (from line 1, column A)', null=True, verbose_name='monetary contributions')),
                ('loans_received', models.IntegerField(help_text='Total loans received (from line 2, column A)', null=True, verbose_name='loans received')),
                ('subtotal_cash_contributions', models.IntegerField(help_text='Monetary contributions and loans received combined (from line 3, column A)', null=True, verbose_name='subtotal cash contributions')),
                ('nonmonetary_contributions', models.IntegerField(help_text='Non-monetary contributions (from line 4, column A)', null=True, verbose_name='nonmonetary contributions')),
                ('total_contributions', models.IntegerField(help_text='Total contributions (from line 5, column A)', null=True, verbose_name='total contributions')),
                ('payments_made', models.IntegerField(help_text='Payments made (from line 6, column A)', null=True, verbose_name='payments made')),
                ('loans_made', models.IntegerField(help_text='Loans made (from line 7, column A)', null=True, verbose_name='loans made')),
                ('subtotal_cash_payments', models.IntegerField(help_text='Sub-total of cash payments (from line 8, column A)', null=True, verbose_name='subtotal cash payments')),
                ('unpaid_bills', models.IntegerField(help_text='Unpaid bills / accrued expenses (from line 9, column A)', null=True, verbose_name='unpaid bills')),
                ('nonmonetary_adjustment', models.IntegerField(help_text='Non-monetary adjustment (from line 10, column A), which is equal to the total of non-monetary contributions', null=True, verbose_name='nonmonetary adjustment')),
                ('total_expenditures_made', models.IntegerField(help_text='Total expenditures made (from line 11, column A)', null=True, verbose_name='total expenditures made')),
                ('begin_cash_balance', models.IntegerField(help_text='Beginning cash balance (from line 12), which is equal to the Ending Cash Balance (line 16) reported on the summary page of the previous Form 460 filing', null=True, verbose_name='begin cash balance')),
                ('cash_receipts', models.IntegerField(help_text='Cash receipts (from line 13)', null=True, verbose_name='cash receipts')),
                ('miscellaneous_cash_increases', models.IntegerField(help_text='Miscellaneous cash increases (from line 14)', null=True, verbose_name='miscellaneous cash increases')),
                ('cash_payments', models.IntegerField(help_text='Cash payments (from line 15)', null=True, verbose_name='cash payments')),
                ('ending_cash_balance', models.IntegerField(help_text='Ending cash balance (from line 16)', null=True, verbose_name='ending cash balance')),
                ('loan_guarantees_received', models.IntegerField(help_text='Loan guarantees received (from line 17)', null=True, verbose_name='loan guarantees received')),
                ('cash_equivalents', models.IntegerField(help_text="Cash equivalents (from line 18), which includes investments that can't be readily converted to cash, such as outstanding loans the committee has made to others", null=True, verbose_name='cash equivalents')),
                ('outstanding_debts', models.IntegerField(help_text='Outstanding debts on loans owed by the committee (from line 19)', null=True, verbose_name='outstanding debts')),
                ('filing_id', models.IntegerField(db_index=True, help_text='Filing identification number', primary_key=True, serialize=False, verbose_name='filing id')),
                ('amendment_count', models.IntegerField(db_index=True, help_text='Number of amendments to this filing.', verbose_name='Count amendments')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='F460FilingVersion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_filed', models.DateField(db_index=True, help_text='Date this report was filed, according to the filer (from CVR_CAMPAIGN_DISCLOSURE.RPT_DATE)', verbose_name='date filed')),
                ('from_date', models.DateField(db_index=True, help_text='The first date of the filing period covered by the statement (from CVR_CAMPAIGN_DISCLOSURE.FROM_DATE)', verbose_name='from date')),
                ('thru_date', models.DateField(db_index=True, help_text='The last date of the filing period covered by the statement (from CVR_CAMPAIGN_DISCLOSURE.THRU_DATE)', verbose_name='thru date')),
                ('filer_id', models.IntegerField(db_index=True, help_text='Numeric filer identification number (from FILER_XREF.FILER_ID)', verbose_name='filer id')),
                ('filer_lastname', models.CharField(help_text='Last name of filer (from CVR_CAMPAIGN_DISCLOSURE.FILER_NAML)', max_length=200, verbose_name='filer last name')),
                ('filer_firstname', models.CharField(blank=True, help_text='First name of the filer (from CVR_CAMPAIGN_DISCLOSURE.FILER_NAMF)', max_length=45, verbose_name='filer first name')),
                ('election_date', models.DateField(db_index=True, help_text='Date of the election in which the filer is participating (from CVR_CAMPAIGN_DISCLOSURE.ELECT_DATE)', null=True, verbose_name='election date')),
                ('monetary_contributions', models.IntegerField(help_text='Total monetary contributions (from line 1, column A)', null=True, verbose_name='monetary contributions')),
                ('loans_received', models.IntegerField(help_text='Total loans received (from line 2, column A)', null=True, verbose_name='loans received')),
                ('subtotal_cash_contributions', models.IntegerField(help_text='Monetary contributions and loans received combined (from line 3, column A)', null=True, verbose_name='subtotal cash contributions')),
                ('nonmonetary_contributions', models.IntegerField(help_text='Non-monetary contributions (from line 4, column A)', null=True, verbose_name='nonmonetary contributions')),
                ('total_contributions', models.IntegerField(help_text='Total contributions (from line 5, column A)', null=True, verbose_name='total contributions')),
                ('payments_made', models.IntegerField(help_text='Payments made (from line 6, column A)', null=True, verbose_name='payments made')),
                ('loans_made', models.IntegerField(help_text='Loans made (from line 7, column A)', null=True, verbose_name='loans made')),
                ('subtotal_cash_payments', models.IntegerField(help_text='Sub-total of cash payments (from line 8, column A)', null=True, verbose_name='subtotal cash payments')),
                ('unpaid_bills', models.IntegerField(help_text='Unpaid bills / accrued expenses (from line 9, column A)', null=True, verbose_name='unpaid bills')),
                ('nonmonetary_adjustment', models.IntegerField(help_text='Non-monetary adjustment (from line 10, column A), which is equal to the total of non-monetary contributions', null=True, verbose_name='nonmonetary adjustment')),
                ('total_expenditures_made', models.IntegerField(help_text='Total expenditures made (from line 11, column A)', null=True, verbose_name='total expenditures made')),
                ('begin_cash_balance', models.IntegerField(help_text='Beginning cash balance (from line 12), which is equal to the Ending Cash Balance (line 16) reported on the summary page of the previous Form 460 filing', null=True, verbose_name='begin cash balance')),
                ('cash_receipts', models.IntegerField(help_text='Cash receipts (from line 13)', null=True, verbose_name='cash receipts')),
                ('miscellaneous_cash_increases', models.IntegerField(help_text='Miscellaneous cash increases (from line 14)', null=True, verbose_name='miscellaneous cash increases')),
                ('cash_payments', models.IntegerField(help_text='Cash payments (from line 15)', null=True, verbose_name='cash payments')),
                ('ending_cash_balance', models.IntegerField(help_text='Ending cash balance (from line 16)', null=True, verbose_name='ending cash balance')),
                ('loan_guarantees_received', models.IntegerField(help_text='Loan guarantees received (from line 17)', null=True, verbose_name='loan guarantees received')),
                ('cash_equivalents', models.IntegerField(help_text="Cash equivalents (from line 18), which includes investments that can't be readily converted to cash, such as outstanding loans the committee has made to others", null=True, verbose_name='cash equivalents')),
                ('outstanding_debts', models.IntegerField(help_text='Outstanding debts on loans owed by the committee (from line 19)', null=True, verbose_name='outstanding debts')),
                ('filing_id', models.IntegerField(db_index=True, help_text='Filing identification number', verbose_name='filing id')),
                ('amend_id', models.IntegerField(db_index=True, help_text='Amendment identification number', verbose_name='amendment id')),
            ],
        ),
        migrations.DeleteModel(
            name='F460Summary',
        ),
        migrations.AlterModelOptions(
            name='scrapedelection',
            options={'ordering': ('-year',)},
        ),
        migrations.AlterModelOptions(
            name='scrapedproposition',
            options={'ordering': ('-election', 'name')},
        ),
        migrations.RemoveField(
            model_name='scrapedelection',
            name='date',
        ),
        migrations.RemoveField(
            model_name='scrapedelection',
            name='election_type',
        ),
        migrations.AddField(
            model_name='scrapedelection',
            name='name',
            field=models.CharField(blank=True, help_text='Scraped election name', max_length=200, verbose_name='scraped election name'),
        ),
        migrations.AlterUniqueTogether(
            name='f460filingversion',
            unique_together=set([('filing_id', 'amend_id')]),
        ),
        migrations.AlterUniqueTogether(
            name='candidatecommittee',
            unique_together=set([('candidate_filer_id', 'committee_filer_id', 'link_type_id')]),
        ),
    ]