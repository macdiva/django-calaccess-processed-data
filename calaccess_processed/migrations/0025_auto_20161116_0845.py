# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-16 08:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calaccess_processed', '0024_election_proposition_propositioncommittee'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CandidateScrapedCommittee',
            new_name='ScrapedCandidateCommittee',
        ),
        migrations.RenameModel(
            old_name='PropositionScrapedCommittee',
            new_name='ScrapedPropositionCommittee',
        ),
    ]